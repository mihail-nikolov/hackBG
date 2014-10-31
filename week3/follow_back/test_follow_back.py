import unittest
from follow_back import Graph


class Graph_tests(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_edge_nodes_exist(self):
        self.graph.nodes = {"Ivan": [], "Georgi": []}
        self.graph.add_edge("Ivan", "Georgi")
        self.assertIn("Georgi", self.graph.nodes["Ivan"])
        self.assertEqual(len(self.graph.nodes["Georgi"]), 0)

    def test_add_edge_nodes_dont_exist(self):
        self.graph.add_edge("Ivan", "Georgi")
        self.assertIn("Georgi", self.graph.nodes["Ivan"])
        self.assertEqual(len(self.graph.nodes["Georgi"]), 0)

    def test_get_neighbours(self):
        self.graph.add_edge("Ivan", "Georgi")
        self.assertEqual(self.graph.get_neighbours_for_node("Ivan"), ["Georgi"])
        self.assertEqual(self.graph.get_neighbours_for_node("Georgi"), [])
        self.assertFalse(self.graph.get_neighbours_for_node("Pesho"))


if __name__ == '__main__':
    unittest.main()
