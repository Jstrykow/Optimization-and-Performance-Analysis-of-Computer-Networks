from re import L
from link import Link
from node import Node


def test_Link():
    link = Link(1, 2, 72, 3, 4)
    assert link.get_start_node_id() == 1
    assert link.get_end_node_id() == 2
    assert link.get_number_of_fibers() == 72
    assert link.get_fiber_cost() == 3
    assert link.get_number_of_lambdas_in_fiber() == 4
    assert str(link) == "Link: start: 1, end: 2, number of fibers: 72, fiber cost: 3, number of lambdas_in_fiber: 4"


def test_node():
    node = Node(1)
    node.add_link(1, 2, 72, 3, 4)
    node.add_link(1, 3, 73, 5, 6)
    assert str(node.links[0]) == "Link: start: 1, end: 2, number of fibers: 72, fiber cost: 3, number of lambdas_in_fiber: 4"
    assert str(node.links[1]) == "Link: start: 1, end: 3, number of fibers: 73, fiber cost: 5, number of lambdas_in_fiber: 6"


def test_node_neighbours():
    node = Node(1)
    node.add_link(1, 2, 72, 3, 4)
    node.add_link(1, 3, 73, 5, 6)
    assert node.neighbours == [2, 3]