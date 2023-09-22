import polygons_share_edge


def test_shared_edges_0():
    square_0 = [(0., 0.), (1., 0.), (1., 1.), (0., 1.), (0., 0.)]
    square_1 = [(1., 0.), (2., 0.), (2., 1.), (1., 1.), (1., 0.)]
    sq_0_x, sq_0_y = zip(*square_0)
    sq_1_x, sq_1_y = zip(*square_1)
    assert polygons_share_edge.share_edge(5, 5, sq_0_x, sq_0_y, sq_1_x,
                                          sq_1_y, int(True))
    return
def test_shared_edges_0():
    square_0 = [(0., 0.), (1., 0.), (1., 1.), (0., 1.), (0., 0.)]
    square_1 = [(1., 0.), (2., 0.), (2., 1.), (1., 1.), (1., 0.)]
    sq_0_x, sq_0_y = zip(*square_0)
    sq_1_x, sq_1_y = zip(*square_1)
    assert not polygons_share_edge.share_edge(5, 5, sq_0_x, sq_0_y, sq_1_x,
                                              sq_1_y, int(False))
    return
def test_shared_edges_2():
    square_0 = [(0., 0.), (1., 0.), (1.1, 1.), (0., 1.), (0., 0.)]
    square_1 = [(1., 0.), (2., 0.), (2., 1.), (1., 1.), (1., 0.)]
    sq_0_x, sq_0_y = zip(*square_0)
    sq_1_x, sq_1_y = zip(*square_1)
    assert not polygons_share_edge.share_edge(5, 5, sq_0_x, sq_0_y, sq_1_x,
                                              sq_1_y, int(True))
    return
