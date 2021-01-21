from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        graph = DiGraph()
        algo = GraphAlgo(graph)
        self.assertEqual(graph, algo.get_graph())
        algo = GraphAlgo()
        self.assertNotEqual(graph, algo.get_graph())

    def test_load_from_json(self):
        graph = DiGraph()
        file = '../data/G_10_80_1.json'
        algo = GraphAlgo(graph)
        algo.load_from_json(file)


    def test_save_to_json(self):
        algo = GraphAlgo()
        file = '../data/G_10_80_1.json'
        algo.load_from_json(file)
        file_to_save = '../data/G_10_80_1.json_edited2'
        algo.save_to_json(file_to_save)

    def test_shortest_path(self):
        graph = DiGraph()
        algo = GraphAlgo(graph)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_edge(2, 3, 1)
        graph.add_edge(2, 4, 5)
        graph.add_edge(3, 4, 100)
        path = algo.shortest_path(2, 4)

        if path[0] is not 5:
            self.fail()

    def test_connected_component(self):
        graph = DiGraph()
        algo = GraphAlgo(graph)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 2, 3)
        print(algo.connected_component(2))


    def test_connected_components(self):
        graph = DiGraph()
        algo = GraphAlgo(graph)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 2, 3)
        print(algo.connected_components())

    def test_plot_graph(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        algo = GraphAlgo(graph)
        algo.plot_graph()

