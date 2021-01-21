from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def test_v_size(self):
        graph = DiGraph()
        self.assertEqual(0, graph.v_size())

        graph.add_node(2)

        self.assertEqual(1, graph.v_size())
        graph.remove_node(2)
        self.assertEqual(0, graph.v_size())

    def test_e_size(self):
        graph = DiGraph()
        graph.add_node(2)

        self.assertEqual(0, graph.e_size())

        graph.add_edge(2, 2, 3)
        self.assertEqual(0, graph.e_size())

        graph.add_node(3)
        graph.add_edge(2, 3, 3)
        self.assertEqual(1, graph.e_size())

    def test_get_all_v(self):
        graph = DiGraph()
        graph.add_node(2, (3, 2))
        graph.add_node(3)
        graph.add_node(4)

        all_v = graph.get_all_v()
        added_nodes = {2, 3, 4}

        if not added_nodes <= set(all_v):
            self.fail()

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(2, (3, 2))
        graph.add_node(3, (3, 2))
        graph.add_node(4, (3, 2))
        graph.add_edge(2, 3, 30)
        graph.add_edge(4, 3, 20)
        # incoming edges for 3 are 2, 4

        incoming = graph.all_in_edges_of_node(3)
        incoming2 = {2: 30, 4: 20}

        for k in incoming:
            if k not in incoming2:
                self.fail()

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(2, (3, 2))
        graph.add_node(3, (3, 2))
        graph.add_node(4, (3, 2))
        graph.add_edge(2, 3, 30)
        graph.add_edge(2, 4, 20)
        # incoming edges for 3 are 2, 4

        outgoing = graph.all_in_edges_of_node(3)
        outgoing2 = {2: 30, 2: 20}

        for k in outgoing:
            if k not in outgoing2:
                self.fail()

    def test_get_mc(self):
        graph = DiGraph()
        self.assertEqual(0, graph.get_mc())
        graph.add_node(2, (3, 2))
        self.assertEqual(1, graph.get_mc())

    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(2)
        graph.add_node(3)
        self.assertTrue(graph.add_edge(2, 3, 2))
        self.assertFalse(graph.add_edge(2, 4, 2))

    def test_add_node(self):
        graph = DiGraph()
        self.assertTrue(graph.add_node(2, (3, 2)))
        self.assertFalse(graph.add_node(2, (3, 2)))

    def test_remove_node(self):
        graph = DiGraph()
        graph.add_node(2)
        node = graph.get_node(2)
        self.assertIsNotNone(node)
        node = graph.get_node(3)
        self.assertIsNone(node)

    def test_remove_edge(self):
        graph = DiGraph()
        graph.add_node(2)
        graph.add_node(3)
        self.assertTrue(graph.add_edge(3, 2, 3))
        self.assertTrue(graph.add_edge(2, 3, 3))
        self.assertFalse(graph.add_edge(3, 3, 3))
        self.assertFalse(graph.add_edge(3, 3, 3))
        self.assertFalse(graph.add_edge(3, 4, 3))

    def test_get_node(self):
        graph = DiGraph()
        graph.add_node(2, (32, 32))
        node = graph.get_node(2)
        self.assertIsNotNone(node)
