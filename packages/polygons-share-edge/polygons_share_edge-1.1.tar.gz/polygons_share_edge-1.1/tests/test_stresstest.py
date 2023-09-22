import polygons_share_edge
import numpy as np

N = 100_000
C_min, C_max = 5, 500

def test_many():
    for i in range(N):
        N_0, N_1 = np.random.randint(C_min, C_max, size=2)
        p0 = np.random.normal(loc=5., scale=3., size=(N_0, 2))
        p0x, p0y = p0.T
        p1 = np.random.normal(loc=5., scale=3., size=(N_1, 2))
        p1x, p1y = p1.T

        p0x = list(p0x[:-1]) + [p0x[0]]
        p0y = list(p0y[:-1]) + [p0y[0]]
        p1x = list(p1x[:-1]) + [p1x[0]]
        p1y = list(p1y[:-1]) + [p1y[0]]
        assert p0x[0] == p0x[-1]
        assert p0y[0] == p0y[-1]
        assert p1x[0] == p1x[-1]
        assert p1y[0] == p1y[-1]
        polygons_share_edge.share_edge(N_0, N_1, p0x, p0y, p1x, p1y, int(True))
    return
