from link import Link


def test_Link():
    link = Link(1, 2, 72, 3, 4)
    assert link.get_start_node_id() == 1
    assert link.get_end_node_id() == 2
    assert link.get_number_of_fibers() == 72
    assert link.get_fiber_cost() == 3
    assert link.get_number_of_lambdas_in_fiber() == 4
    