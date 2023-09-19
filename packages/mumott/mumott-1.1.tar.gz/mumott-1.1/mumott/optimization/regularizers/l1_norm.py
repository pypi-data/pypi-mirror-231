from typing import Dict

import numpy as np
from numpy.typing import NDArray

from ..regularizers.base_regularizer import Regularizer


class L1Norm(Regularizer):

    r"""Regularizes using the :math:`L_1` norm of the coefficient vector, also known as the
    Manhattan or taxicab norm.
    Suitable for scalar fields or tensor fields in local representations. Tends to reduce noise.

    The :math:`L_1` norm of a vector :math:`x` is given by :math:`\sum{\vert x \vert}`.

    See also `this Wikipedia article <https://en.wikipedia.org/wiki/Taxicab_geometry>`_.
    """

    def __init__(self):
        super().__init__()

    def get_regularization_norm(self,
                                coefficients: NDArray[float],
                                get_gradient: bool = False) -> Dict:
        """Retrieves the :math:`L_1` norm, also called the Manhattan or taxicab norm, of the
        coefficients. Appropriate for use with scalar fields or tensor fields in local basis sets.

        Parameters
        ----------
        coefficients
            An ``np.ndarray`` of values, with shape ``(X, Y, Z, W)``, where
            the last channel contains, e.g., tensor components.
        get_gradient
            If ``True``, returns a ``'gradient'`` of the same shape as :attr:`coefficients`.
            Otherwise the entry ``'gradient'`` will be ``None``. Defaults to ``False``.

        Returns
        -------
            A dictionary with two entries, ``regularization_norm`` and ``gradient``.
        """
        result = dict(regularization_norm=None, gradient=None)
        if get_gradient:
            result['gradient'] = np.sign(coefficients)
        result['regularization_norm'] = np.sum(np.abs(coefficients))
        return result

    @property
    def _function_as_str(self) -> str:
        return 'R(x) = lambda * abs(x)'

    @property
    def _function_as_tex(self) -> str:
        return r'$R(\vec{x}) = \lambda \Vert \vec{x} \Vert_1$'
