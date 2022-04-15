from link import Link
from node import Node
from graph import Graph

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


def test_graph():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_1.add_link(1, 2, 72, 3, 4)
    node_1.add_link(1, 3, 73, 5, 6)
    node_2.add_link(2, 1, 72, 3, 4)
    node_3.add_link(3, 1, 73, 5, 6)
    graph = Graph()
    graph.add_nodes(node_1)
    graph.add_nodes(node_2)
    graph.add_nodes(node_3)
    assert graph.get_nodes() == "Node ID:1, neighbours [2, 3]\nNode ID:2, neighbours [1]\nNode ID:3, neighbours [1]\n"