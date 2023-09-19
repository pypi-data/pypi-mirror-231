from typing import Any

from math import floor
from numba import config, cuda, int32, float32, float64, void
from numpy.typing import NDArray
import numpy as np


def _is_cuda_array(item: Any):
    """ Internal method which assists in debugging. """
    if config.ENABLE_CUDASIM:
        return False
    else:
        return cuda.is_cuda_array(item)


def john_transform_cuda(field: NDArray, projections: NDArray, unit_vector_p: NDArray,
                        unit_vector_j: NDArray, unit_vector_k: NDArray, offsets_j: NDArray,
                        offsets_k: NDArray):
    """ Frontend for performing the John transform with parallel
    GPU computing.

    Parameters
    ----------
    field
        The field to be projected, with 4 dimensions. The last index should
        have the same size as the last index of ``projections``. Can be either
        a `numpy.ndarray`, or a device array that implements the CUDA array
        interface. If a device array is given, no copying to device is needed.
    projections
        A 4-dimensional numpy array where the projections are stored.
        The first index runs over the different projection directions. Can be either
        a `numpy.ndarray`, or a device array that implements the CUDA array
        interface. If a device array is given, no copying or synchronization is needed.
    unit_vector_p
        The direction of projection in Cartesian coordinates.
    unit_vector_j
        One of the directions for the pixels of ``projection``.
    unit_vector_k
        The other direction for the pixels of ``projection``.
    offsets_j
        Offsets which align projections in the direction of `j`
    offsets_k
        Offsets which align projections in the direction of `k`.

    Notes
    -----
    For mathematical details, see the :meth:<`~.john_transform.john_transform`.
    """
    # Always false for now as we are sticking to ``float32``.
    if False:
        cuda_float = float64
        numpy_float = np.float64
        cuda_x4_type = cuda.float64x4
    else:
        cuda_float = float32
        numpy_float = np.float32
        cuda_x4_type = cuda.float32x4

    # Find zeroth, first and second directions for indexing. Zeroth is the maximal projection direction.

    # (x, y, z), (y, x, z), (z, x, y)
    direction_0_index = np.argmax(abs(unit_vector_p), axis=1).reshape(-1, 1).astype(np.int32)
    direction_1_index = 1 * (direction_0_index == 0).astype(np.int32).reshape(-1, 1).astype(np.int32)
    direction_2_index = (2 - (direction_0_index == 2)).astype(np.int32).reshape(-1, 1).astype(np.int32)

    # Step size for direction 1 and 2.
    step_sizes_1 = (np.take_along_axis(unit_vector_p, direction_1_index, 1) /
                    np.take_along_axis(unit_vector_p, direction_0_index, 1)).astype(numpy_float).ravel()
    step_sizes_2 = (np.take_along_axis(unit_vector_p, direction_2_index, 1) /
                    np.take_along_axis(unit_vector_p, direction_0_index, 1)).astype(numpy_float).ravel()

    # Shape in each of the three directions.
    dimensions_0 = np.array(field.shape, dtype=numpy_float)[direction_0_index.ravel()]
    dimensions_1 = np.array(field.shape, dtype=numpy_float)[direction_1_index.ravel()]
    dimensions_2 = np.array(field.shape, dtype=numpy_float)[direction_2_index.ravel()]

    # Correction factor for length of line when taking a one-slice step.
    distance_multipliers = np.sqrt(1.0 + step_sizes_1 ** 2 + step_sizes_2 ** 2).astype(numpy_float)

    max_index = projections.shape[0]
    max_j = projections.shape[1]
    max_k = projections.shape[2]

    # CUDA chunking and memory size constants.
    channels = int(field.shape[-1])
    blocks_j = int(32)
    blocks_k = int(32)
    blocks_angle = int(8)

    # Indices to navigate each projection. s is the surface positioning.
    k_vectors = unit_vector_k.astype(numpy_float)
    j_vectors = unit_vector_j.astype(numpy_float)
    s_vectors = (unit_vector_k * (-0.5 * max_k + offsets_k.reshape(-1, 1)) +
                 unit_vector_j * (-0.5 * max_j + offsets_j.reshape(-1, 1))).astype(numpy_float)

    # (0, 1, 2) if x main, (1, 0, 2) if y main, (2, 0, 1) if z main.
    direction_indices = np.stack((direction_0_index.ravel(),
                                  direction_1_index.ravel(),
                                  direction_2_index.ravel()), axis=1)

    # Bilinear interpolation over each slice.

    @cuda.jit(void(cuda_float[:, :, :, ::1], int32, cuda_float,
              cuda_float, cuda_float, int32[::1], cuda_float[::1]), device=True)
    def bilinear_interpolation(field: NDArray,
                               direction_0,
                               r0: float,
                               r1: float,
                               r2: float,
                               dimensions,
                               accumulator: NDArray):
        """ Kernel for bilinear interpolation. Replaces texture interpolation."""
        if not (-1 <= r1 < dimensions[1] and -1 <= r2 < dimensions[2]):
            return
        # At edges, interpolate between value and 0.
        if (0 <= r1 < dimensions[1] - 1):
            r1_weight = int32(1)
        else:
            r1_weight = int32(0)

        if (0 <= r2 < dimensions[2] - 1):
            r2_weight = int32(1)
        else:
            r2_weight = int32(0)

        if -1 < r1 < 0:
            r1_edge_weight = int32(1)
        else:
            r1_edge_weight = int32(0)

        if -1 < r2 < 0:
            r2_edge_weight = int32(1)
        else:
            r2_edge_weight = int32(0)

        weight_1 = cuda_float((r1 - floor(r1)) * r1_weight) * (1 - r1_edge_weight)
        weight_2 = cuda_float((r2 - floor(r2)) * r2_weight) * (1 - r2_edge_weight)
        t = cuda_x4_type((1 - weight_1) * (1 - weight_2),
                         (weight_1 * weight_2),
                         ((1 - weight_1) * weight_2),
                         ((1 - weight_2) * weight_1))
        # Branch should be abstracted away by compiler, but could be done with pointer arithmetic.
        if (direction_0 == 0):
            x = int32(floor(r0))
            y = int32(floor(r1) + r1_edge_weight)
            y2 = y + r1_weight
            z = int32(floor(r2) + r2_edge_weight)
            z2 = z + r2_weight
            for i in range(accumulator.size):
                accumulator[i] += field[x, y, z, i] * t.x
                accumulator[i] += field[x, y2, z, i] * t.w
                accumulator[i] += field[x, y, z2, i] * t.z
                accumulator[i] += field[x, y2, z2, i] * t.y

        elif (direction_0 == 1):
            x = int32(floor(r1) + r1_edge_weight)
            x2 = x + r1_weight
            y = int32(floor(r0))
            z = int32(floor(r2) + r2_edge_weight)
            z2 = z + r2_weight
            for i in range(accumulator.size):
                accumulator[i] += field[x, y, z, i] * t.x
                accumulator[i] += field[x2, y, z, i] * t.w
                accumulator[i] += field[x, y, z2, i] * t.z
                accumulator[i] += field[x2, y, z2, i] * t.y

        elif (direction_0 == 2):
            x = int32(floor(r1) + r1_edge_weight)
            x2 = x + r1_weight
            y = int32(floor(r2) + r2_edge_weight)
            y2 = y + r2_weight
            z = int32(floor(r0))
            for i in range(accumulator.size):
                accumulator[i] += field[x, y, z, i] * t.x
                accumulator[i] += field[x2, y, z, i] * t.w
                accumulator[i] += field[x, y2, z, i] * t.z
                accumulator[i] += field[x2, y2, z, i] * t.y

    @cuda.jit(void(cuda_float[:, :, :, ::1], cuda_float[:, :, :, ::1]), cache=True)
    def john_transform_inner(field: NDArray, projection: NDArray):
        """ Performs the John transform of a field. Relies on a large number
        of pre-defined constants outside the kernel body. """
        index = cuda.blockIdx.y * blocks_angle + cuda.threadIdx.y
        j = cuda.threadIdx.x + blocks_j * (
                cuda.blockIdx.x % (
                    (max_j + blocks_j - 1) // blocks_j))

        if (j >= max_j) or (index >= max_index):
            return

        start_k = blocks_k * (cuda.blockIdx.x // (
            (max_j + blocks_j - 1) // blocks_j))
        end_k = start_k + blocks_k
        if end_k > max_k:
            end_k = max_k

        if start_k >= end_k:
            return

        # Define compile-time constants.
        step_size_1 = step_sizes_1[index]
        step_size_2 = step_sizes_2[index]
        k_vectors_c = k_vectors[index]
        j_vectors_c = j_vectors[index]
        s_vectors_c = s_vectors[index]
        dimensions_0_c = dimensions_0[index]
        dimensions_1_c = dimensions_1[index]
        dimensions_2_c = dimensions_2[index]
        dimensions = cuda.local.array(3, int32)
        dimensions[0] = dimensions_0_c
        dimensions[1] = dimensions_1_c
        dimensions[2] = dimensions_2_c
        direction_indices_c = direction_indices[index]
        distance_multiplier = distance_multipliers[index]

        # Could be chunked for very asymmetric samples.
        start_slice = 0
        end_slice = start_slice + dimensions[0]
        accumulator = cuda.local.array(channels, cuda_float)

        for k in range(start_k, end_k):
            for i in range(channels):
                accumulator[i] = 0.

            fj = cuda_float(j) + 0.5
            fk = cuda_float(k) + 0.5

            # Initial coordinates of projection.
            start_position_0 = (s_vectors_c[direction_indices_c[0]] +
                                fj * j_vectors_c[direction_indices_c[0]] +
                                fk * k_vectors_c[direction_indices_c[0]])
            start_position_1 = (s_vectors_c[direction_indices_c[1]] +
                                fj * j_vectors_c[direction_indices_c[1]] +
                                fk * k_vectors_c[direction_indices_c[1]])
            start_position_2 = (s_vectors_c[direction_indices_c[2]] +
                                fj * j_vectors_c[direction_indices_c[2]] +
                                fk * k_vectors_c[direction_indices_c[2]])

            # Centering w.r.t volume.

            position_0 = cuda_float(start_slice) + 0.5
            position_1 = cuda_float(step_size_1 * (cuda_float(start_slice) -
                                    0.5 * dimensions[0] - start_position_0 + 0.5) +
                                    start_position_1 + 0.5 * dimensions[1] - 0.5)
            position_2 = cuda_float(step_size_2 * (cuda_float(start_slice) -
                                    0.5 * dimensions[0] -
                                    start_position_0 + 0.5) +
                                    start_position_2 + 0.5 * dimensions[2] - 0.5)

            for i in range(start_slice, end_slice):
                bilinear_interpolation(field, direction_indices_c[0],
                                       position_0, position_1, position_2, dimensions, accumulator)
                position_0 += cuda_float(1.0)
                position_1 += step_size_1
                position_2 += step_size_2

            for i in range(channels):
                projection[index, j, k, i] += accumulator[i] * distance_multiplier

    # Launching of kernel.
    bpg = (((max_j + blocks_j - 1) // blocks_j) *
           ((max_k + blocks_k - 1) // blocks_k),
           ((projections.shape[0] + blocks_angle - 1) // blocks_angle))
    tpb = (blocks_j, blocks_angle)
    john_transform_grid = john_transform_inner[bpg, tpb]

    def transform_with_transfer(field: NDArray[float], projections: NDArray[float]):
        if _is_cuda_array(field):
            assert field.dtype == 'float32'
            device_field = cuda.as_cuda_array(field)
        else:
            assert field.dtype == np.float32
            device_field = cuda.to_device(field)

        if _is_cuda_array(projections):
            assert projections.dtype == 'float32'
            device_projections = cuda.as_cuda_array(projections)
            transfer_projections = False
        else:
            assert projections.dtype == np.float32
            device_projections = cuda.to_device(projections)
            transfer_projections = True

        john_transform_grid(device_field, device_projections)
        if transfer_projections:
            device_projections.copy_to_host(projections)

    return transform_with_transfer


def john_transform_adjoint_cuda(field: NDArray, projections: NDArray, unit_vector_p: NDArray,
                                unit_vector_j: NDArray, unit_vector_k: NDArray, offsets_j: NDArray,
                                offsets_k: NDArray):
    """ Frontend for performing the adjoint of the John transform with parallel
    GPU computing.

    Parameters
    ----------
    field
        The field into which the adjoint is projected, with 4 dimensions. The last index should
        have the same size as the last index of ``projections``. Can be either
        a `numpy.ndarray`, or a device array that implements the CUDA array
        interface. If a device array is given, no copying to device is needed.
    projections
        The projections from which the adjoint is calculated.
        The first index runs over the different projection directions. Can be either
        a `numpy.ndarray`, or a device array that implements the CUDA array
        interface. If a device array is given, no copying or synchronization is needed.
    unit_vector_p
        The direction of projection in Cartesian coordinates.
    unit_vector_j
        One of the directions for the pixels of ``projection``.
    unit_vector_k
        The other direction for the pixels of ``projection``.
    offsets_j
        Offsets which align projections in the direction of `j`
    offsets_k
        Offsets which align projections in the direction of `k`.

    Notes
    -----
    For mathematical details, see the :meth:<`~.john_transform.john_transform_adjoint`.
    """
    # Always false as we are sticking to float32
    if False:
        cuda_float = float64
        numpy_float = np.float64
        cuda_x4_type = cuda.float64x4
    else:
        cuda_float = float32
        numpy_float = np.float32
        cuda_x4_type = cuda.float32x4

    max_j = projections.shape[1]
    max_k = projections.shape[2]
    # CUDA chunking and memory size constants.
    blocks_z = int(1)
    # blocks_angle = int(512)  # Not used for now.
    blocks_x = int(16)
    blocks_y = int(16)

    # Projection vectors. s for positioning the projection.
    p_vectors = unit_vector_p.astype(numpy_float)
    k_vectors = unit_vector_k.astype(numpy_float)
    j_vectors = unit_vector_j.astype(numpy_float)
    s_vectors = (unit_vector_k * (-0.5 * max_k + offsets_k.reshape(-1, 1)) +
                 unit_vector_j * (-0.5 * max_j + offsets_j.reshape(-1, 1))).astype(numpy_float)

    # Translate volume steps to normalized projection steps. Can add support for non-square voxels.
    vector_norm = np.einsum('...i, ...i', p_vectors, np.cross(j_vectors, k_vectors))
    norm_j = -np.cross(p_vectors, k_vectors) / vector_norm[..., None]
    norm_k = np.cross(p_vectors, j_vectors) / vector_norm[..., None]
    norm_offset_j = -np.einsum('...i, ...i', p_vectors, np.cross(s_vectors, k_vectors)) / vector_norm
    norm_offset_k = np.einsum('...i, ...i', p_vectors, np.cross(s_vectors, j_vectors)) / vector_norm

    channels = field.shape[-1]

    @cuda.jit(void(cuda_float[:, :, :, ::1], cuda_float,
                   cuda_float, cuda_float, cuda_float[::1]), device=True)
    def bilinear_interpolation_projection(projection: NDArray,
                                          r0: float,
                                          r1: float,
                                          r2: float,
                                          accumulator: NDArray):
        if not (-1 <= r1 < max_j and -1 <= r2 < max_k):
            return
        # At edges, use nearest-neighbor interpolation.
        if (0 <= r1 + 1 < max_j):
            r1_weight = int32(1)
        else:
            r1_weight = int32(0)

        if (0 <= r2 + 1 < max_k):
            r2_weight = int32(1)
        else:
            r2_weight = int32(0)

        if -1 < r1 < 0:
            r1_edge_weight = 1
        else:
            r1_edge_weight = 0

        if -1 < r2 < 0:
            r2_edge_weight = 1
        else:
            r2_edge_weight = 0

        y_weight = cuda_float((r1 - floor(r1)) * r1_weight) * (1 - r1_edge_weight)
        z_weight = cuda_float((r2 - floor(r2)) * r2_weight) * (1 - r2_edge_weight)
        x = int32(floor(r0))
        y = int32(floor(r1) + r1_edge_weight)
        y2 = y + r1_weight
        z = int32(floor(r2) + r2_edge_weight)
        z2 = z + r2_weight
        t = cuda_x4_type((1 - z_weight) * (1 - y_weight),
                         (z_weight * y_weight),
                         ((1 - z_weight) * y_weight),
                         ((1 - y_weight) * z_weight))
        for i in range(channels):
            accumulator[i] += projection[x, y, z, i] * t.x
            accumulator[i] += projection[x, y2, z, i] * t.z
            accumulator[i] += projection[x, y, z2, i] * t.w
            accumulator[i] += projection[x, y2, z2, i] * t.y

    @cuda.jit(void(cuda_float[:, :, :, ::1], cuda_float[:, :, :, ::1], int32, int32), cache=True)
    def john_transform_adjoint_inner(field: NDArray, projection: NDArray, start_index: int, stop_index: int):
        """ Performs the John transform of a field. Relies on a large number
        of pre-defined constants outside the kernel body. """
        # Indexing of volume coordinates.
        x = cuda.threadIdx.x + blocks_x * (cuda.blockIdx.x % (
                       (field.shape[0] + blocks_x - 1) // blocks_x))
        y = cuda.threadIdx.y + blocks_y * (cuda.blockIdx.x // (
                       (field.shape[0] + blocks_x - 1) // blocks_x))
        if (x >= field.shape[0]) or (y >= field.shape[1]):
            return

        # Stride in z.
        z = cuda.blockIdx.y * blocks_z
        if z >= field.shape[2]:
            return

        # Center of voxel and coordinate system.
        fx = x - 0.5 * field.shape[0] + 0.5
        fy = y - 0.5 * field.shape[1] + 0.5
        fz = z - 0.5 * field.shape[2] + 0.5

        z_acc = cuda.local.array(channels, cuda_float)
        for j in range(channels):
            z_acc[j] = 0.0

        # Compile time constants
        norm_j_c = norm_j[start_index:stop_index]
        norm_k_c = norm_k[start_index:stop_index]
        norm_offset_j_c = norm_offset_j[start_index:stop_index]
        norm_offset_k_c = norm_offset_k[start_index:stop_index]

        for a in range(start_index, stop_index):
            # Center with respect to projection.
            fj = norm_offset_j_c[a] + fx * norm_j_c[a][0] + fy * norm_j_c[a][1] + fz * norm_j_c[a][2] - 0.5
            fk = norm_offset_k_c[a] + fx * norm_k_c[a][0] + fy * norm_k_c[a][1] + fz * norm_k_c[a][2] - 0.5
            bilinear_interpolation_projection(projection,
                                              a, fj, fk, z_acc)
        for i in range(channels):
            field[x, y, z, i] += z_acc[i]

    bpg = (((field.shape[0] + blocks_x - 1) // blocks_x) *
           ((field.shape[1] + blocks_y - 1) // blocks_y),
           ((field.shape[2] + blocks_z - 1) // blocks_z))
    tpb = (blocks_x, blocks_y)
    # Last two arguments hardcoded for now, until I work out how to do chunking efficiently.
    john_transform_adjoint_grid = john_transform_adjoint_inner[bpg, tpb]

    def transform_with_transfer(field: NDArray[float], projections: NDArray[float]):
        if _is_cuda_array(field):
            assert field.dtype == 'float32'
            device_field = cuda.as_cuda_array(field)
            transfer_field = False
        else:
            assert field.dtype == np.float32
            device_field = cuda.to_device(field)
            transfer_field = True

        if _is_cuda_array(projections):
            assert projections.dtype == 'float32'
            device_projections = cuda.as_cuda_array(projections)
        else:
            assert projections.dtype == np.float32
            device_projections = cuda.to_device(projections)

        john_transform_adjoint_grid(device_field,
                                    device_projections,
                                    int32(0), int32(projections.shape[0]))
        if transfer_field:
            device_field.copy_to_host(field)

    return transform_with_transfer
