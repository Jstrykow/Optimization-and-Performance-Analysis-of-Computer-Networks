from network.Link import Link
from network.Demand import Demand
from network.Path import Path


def test_Link():
    link = Link(1, 2, 72, 3, 4)
    assert link.get_start_node_id() == 1
    assert link.get_end_node_id() == 2
    assert link.get_number_of_fibers() == 72
    assert link.get_fiber_cost() == 3
    assert link.get_number_of_lambdas_in_fiber() == 4
    assert str(link) == "Link: start: 1, end: 2, number of fibers: 72, fiber cost: 3, number of lambdas_in_fiber: 4"


def test_Demand():
    demand = Demand(1, 2, 3)
    assert demand.start_node == 1
    assert demand.end_node == 2
    assert demand.demand_volume == 3


def test_Path():
    path = Path(1, [2, 3])
    assert path.path_id == 1
    assert path.links_list == [2, 3]
