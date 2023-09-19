import pytest
import numpy as np

from mumott.data_handling.geometry import GeometryTuple
from mumott.methods.projectors.saxs_projector_astra import SAXSProjectorAstra as SAXSProjectorAstra
from mumott.data_handling import DataContainer


@pytest.fixture
def dc():
    return DataContainer('tests/test_half_circle.h5')


@pytest.fixture
def gm(dc):
    return dc.geometry


fields = [np.arange(128).reshape(4, 4, 4, 2)]

bad_field = [np.arange(72).reshape(4, 3, 3, 2)]

bad_field_projs = [np.array([[[[9.15098953, 10.62922668],
                               [21.25845337, 24.21492577],
                               [27.17140007, 30.12787437],
                               [15.06393719, 16.54217339]],
                              [[36.04082108, 37.54252243],
                               [75.08504486, 78.08844757],
                               [81.09185028, 84.09524536],
                               [42.04762268, 43.54932404]],
                              [[63.07143784, 64.57313538],
                               [129.14627075, 132.14967346],
                               [135.15307617, 138.15647888],
                               [69.07823944, 70.5799408]],
                              [[88.20146179,  89.67578888],
                               [179.35157776, 182.30023193],
                               [185.24888611, 188.19754028],
                               [94.09877014,  95.5730896]]]])]

projs = [np.array([[[[48.83656311, 52.73942184],
                   [56.64228058, 60.54513931],
                   [64.44799805, 68.35085297],
                   [72.25371552, 76.15657043]],
                  [[176.1995697, 180.20410156],
                   [184.20864868, 188.21318054],
                   [192.2177124, 196.22224426],
                   [200.22677612, 204.23132324]],
                  [[304.34472656, 308.34924316],
                   [312.35379028, 316.35830688],
                   [320.362854, 324.36740112],
                   [328.37191772, 332.37646484]],
                  [[419.50640869, 423.40924072],
                   [427.31210327, 431.21496582],
                   [435.11782837, 439.02069092],
                   [442.92355347, 446.82641602]]]])]

adjs = [np.array([[[[45.40274048, 49.03118134],
                   [52.65961838, 56.28805923],
                   [59.91650009, 63.54493332],
                   [67.17337799, 70.80181122]],
                  [[47.69195557, 51.50334167],
                   [55.31472778, 59.12611389],
                   [62.9375, 66.74887848],
                   [70.56027222, 74.3716507]],
                  [[52.3191452, 56.22478485],
                   [60.1304245, 64.03606415],
                   [67.9417038, 71.84733582],
                   [75.75297546, 79.65861511]],
                  [[58.28928757, 62.19969177],
                   [66.11009979, 70.02050018],
                   [73.9309082, 77.84130859],
                   [81.75171661, 85.662117]]],
                 [[[167.24435425, 171.24174],
                   [175.23913574, 179.23652649],
                   [183.23390198, 187.23129272],
                   [191.22866821, 195.22607422]],
                  [[173.2144928, 177.21664429],
                   [181.21881104, 185.22096252],
                   [189.22311401, 193.2252655],
                   [197.22740173, 201.22956848]],
                  [[179.20297241, 183.20750427],
                   [187.21205139, 191.21658325],
                   [195.22111511, 199.22564697],
                   [203.23017883, 207.23472595]],
                  [[185.20977783, 189.21430969],
                   [193.21885681, 197.22338867],
                   [201.22792053, 205.23245239],
                   [209.23698425, 213.24153137]]],
                 [[[295.33453369, 299.33905029],
                   [303.34359741, 307.34811401],
                   [311.35266113, 315.35720825],
                   [319.36172485, 323.36627197]],
                  [[301.34133911, 305.34585571],
                   [309.35040283, 313.35491943],
                   [317.35946655, 321.36401367],
                   [325.36853027, 329.37307739]],
                  [[307.04382324, 311.04595947],
                   [315.04812622, 319.05026245],
                  [323.0524292, 327.05459595],
                  [331.05673218, 335.05889893]],
                  [[312.44204712, 316.43939209],
                  [320.4367981, 324.43417358],
                   [328.43154907, 332.42895508],
                   [336.42633057, 340.42373657]]],
                 [[[410.95925903, 414.86962891],
                   [418.7800293, 422.69046021],
                  [426.6008606, 430.51126099],
                  [434.42166138, 438.33209229]],
                  [[416.35745239, 420.26306152],
                   [424.16870117, 428.07434082],
                   [431.98001099, 435.88565063],
                  [439.79129028, 443.69692993]],
                  [[409.67422485, 413.4855957],
                   [417.29696655, 421.10836792],
                   [424.91976929, 428.73114014],
                   [432.5425415, 436.35391235]],
                 [[390.00985718, 393.63827515],
                  [397.26672363, 400.89517212],
                  [404.52362061, 408.15203857],
                  [411.78048706, 415.40893555]]]])]

bad_projs = [np.arange(24).reshape(1, 4, 3, 2)]

bad_adjs = [np.array([[[[0., 0.46484375],
                     [0.929687,  1.859375],
                     [2.789062,  3.71875],
                     [1.859375,  2.32421875]],
                    [[0.,  0.48828125],
                     [0.976562,  1.953125],
                     [2.929687,  3.90625],
                     [1.953125,  2.44140625]],
                    [[0.09375,  0.59375],
                     [1.1875,  2.1875],
                     [3.1875,  4.1875],
                     [2.09375,  2.59375]],
                    [[0.234375,  0.734375],
                     [1.46875,  2.46875],
                     [3.46875,  4.46875],
                     [2.234375,  2.734375]]],
                   [[[2.789062,  3.2890625],
                     [6.578125,  7.578125],
                     [8.578125,  9.578125],
                     [4.789062,  5.2890625]],
                    [[2.929687,  3.4296875],
                     [6.859375,  7.859375],
                     [8.859375,  9.859375],
                     [4.929687,  5.4296875]],
                    [[3.070312,  3.5703125],
                     [7.140625,  8.140625],
                     [9.140625, 10.140625],
                     [5.070312,  5.5703125]],
                    [[3.210937,  3.7109375],
                     [7.421875,  8.421875],
                     [9.421875, 10.421875],
                     [5.210937,  5.7109375]]],
                   [[[5.789062,  6.2890625],
                     [12.578125, 13.578125],
                     [14.578125, 15.578125],
                     [7.7890625,  8.2890625]],
                    [[5.9296875,  6.4296875],
                     [12.859375, 13.859375],
                     [14.859375, 15.859375],
                     [7.9296875,  8.4296875]],
                    [[6.0703125,  6.5703125],
                     [13.140625, 14.140625],
                     [15.140625, 16.140625],
                     [8.0703125,  8.5703125]],
                    [[6.2109375,  6.7109375],
                     [13.421875, 14.421875],
                     [15.421875, 16.421875],
                     [8.2109375,  8.7109375]]],
                   [[[8.7890625,  9.2890625],
                     [18.578125, 19.578125],
                     [20.578125, 21.578125],
                     [10.7890625, 11.2890625]],
                    [[8.9296875,  9.4296875],
                     [18.859375, 19.859375],
                     [20.859375, 21.859375],
                     [10.9296875, 11.4296875]],
                    [[8.7890625,  9.27734375],
                     [18.5546875, 19.53125],
                     [20.5078125, 21.484375],
                     [10.7421875, 11.23046875]],
                    [[8.3671875,  8.83203125],
                     [17.6640625, 18.59375],
                     [19.5234375, 20.453125],
                     [10.2265625, 10.69140625]]]])]


@pytest.mark.parametrize('field, proj', [f for f in zip(fields, projs)])
def test_forward(field, proj, gm):
    pr = SAXSProjectorAstra(gm)
    assert np.allclose(proj, pr.forward(field))


@pytest.mark.parametrize('field, expected', [f for f in zip(bad_field, bad_field_projs)])
def test_forward_failure(field, expected, gm):
    pr = SAXSProjectorAstra(gm)
    with pytest.raises(ValueError, match='volume shape expected'):
        pr.forward(field)
    gm.volume_shape = np.array(field.shape[:-1])
    proj = pr.forward(field)
    assert np.allclose(proj, expected)


@pytest.mark.parametrize('proj, adj', [f for f in zip(projs, adjs)])
def test_adj(proj, adj, gm):
    pr = SAXSProjectorAstra(gm)
    assert np.allclose(adj, pr.adjoint(proj))


@pytest.mark.parametrize('proj, expected', [f for f in zip(bad_projs, bad_adjs)])
def test_adj_failure(proj, expected, gm):
    pr = SAXSProjectorAstra(gm)
    with pytest.raises(ValueError, match='projection shape expected'):
        pr.adjoint(proj)
    gm.projection_shape = np.array(proj.shape[1:-1])
    adj = pr.adjoint(proj)
    assert np.allclose(adj, expected)


@pytest.mark.parametrize('proj, adj', [f for f in zip(projs, adjs)])
def test_bad_index(proj, adj, gm):
    gm.append(GeometryTuple())
    pr = SAXSProjectorAstra(gm)
    with pytest.raises(NotImplementedError, match='computation of individual'):
        pr.adjoint(proj, indices=np.array((0,)))
    with pytest.raises(NotImplementedError, match='computation of individual'):
        pr.forward(adj, indices=np.array((0,)))


def test_str(gm):
    pr = SAXSProjectorAstra(gm)
    string = str(pr)
    assert '1c5a6b' in string


def test_html(gm):
    pr = SAXSProjectorAstra(gm)
    html = pr._repr_html_()
    assert '1c5a6b' in html
