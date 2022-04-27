from network.Link import Link
from network.Demand import Demand
from network.Path import Path
from network.Chromosome import Chromosome
from network.Net import Net
from network.Solution import Solution


# not working link and demand id added

def test_Link():
    link = Link(1, 1, 2, 72, 3, 4)
    assert link.link_id == 1
    assert link.get_start_node_id() == 1
    assert link.get_end_node_id() == 2
    assert link.get_number_of_fibers() == 72
    assert link.get_fiber_cost() == 3
    assert link.get_number_of_lambdas_in_fiber() == 4
    assert str(link) == "Link: start: 1, end: 2, number of fibers: 72, fiber cost: 3, number of lambdas_in_fiber: 4"


def test_Demand():
    demand = Demand(1, 1, 2, 3)
    assert demand.demand_id == 1
    assert demand.start_node == 1
    assert demand.end_node == 2
    assert demand.demand_volume == 3


def test_Path():
    path = Path(1, [2, 3])
    assert path.path_id == 1
    assert path.links_list == [2, 3]

def test_network():
    net = Net()
    links = []
    links.append(Link(1, 1, 2, 72, 3, 4))
    links.append(Link(2, 4, 5, 73, 7, 8))
    path_1 = Path(1, [2, 3])
    path_2 = Path(2, [1, 2, 3])
    paths = [path_1, path_2]
    demands = []
    d1 = Demand(1, 1, 2, 3)
    d1.paths_list = [path_1]
    d2 = Demand(2, 2, 3, 4)
    d2.paths_list = paths
    demands.append(d1)
    demands.append(d2)
    net.links = links
    net.demands = demands
    assert net.links[0].get_start_node_id() == 1
    assert net.links[0].get_end_node_id() == 2
    assert net.links[0].get_number_of_fibers() == 72
    assert net.links[0].get_fiber_cost() == 3
    assert net.links[0].get_number_of_lambdas_in_fiber() == 4
    msg = 'Link: start: 1, end: 2, number of fibers: 72, fiber cost: 3, number of lambdas_in_fiber: 4\nLink: start: 4, end: 5, number of fibers: 73, fiber cost: 7, number of lambdas_in_fiber: 8\nstart node: 1, end node: 2, demand_volume: 3, paths list:  path id: 1, link list: [2, 3] \nstart node: 2, end node: 3, demand_volume: 4, paths list:  path id: 1, link list: [2, 3]  path id: 2, link list: [1, 2, 3] \n'
    assert str(net) == msg


def test_chromosome():
    net = Net()
    links = []
    links.append(Link(1, 1, 2, 72, 3, 4))
    links.append(Link(2, 4, 5, 73, 7, 8))
    path_1 = Path(1, [2, 3])
    path_2 = Path(2, [1, 2, 3])
    paths = [path_1, path_2]
    demands = []
    d1 = Demand(1, 1, 2, 3)
    d1.paths_list = [path_1]
    d2 = Demand(2, 2, 3, 4)
    d2.paths_list = paths
    demands.append(d1)
    demands.append(d2)
    net.links = links
    net.demands = demands
    pass


sol = Solution(1, 2, 3)