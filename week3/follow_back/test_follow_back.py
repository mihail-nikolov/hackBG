import unittest
from follow_back import DirectedGraph


class Graph_tests(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

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

    def test_path_between_without_loop_false(self):
        self.graph.add_edge("Ivan", "Georgi")
        self.graph.add_edge("Ivan", "Pesho")
        self.graph.add_edge("Ivan", "Misho")
        self.graph.add_edge("Stamat", "Lubo")
        self.graph.add_edge("Stamat", "Stamen")
        self.assertFalse(self.graph.path_between("Ivan", "Stamen"))
        self.assertFalse(self.graph.path_between("Misho", "Stamen"))

    def test_path_between_with_loop_false(self):
        self.graph.add_edge("Ivan", "Georgi")
        self.graph.add_edge("Ivan", "Pesho")
        self.graph.add_edge("Ivan", "Misho")
        self.graph.add_edge("Stamat", "Lubo")
        self.graph.add_edge("Stamat", "Stamen")
        self.assertFalse(self.graph.path_between("Ivan", "Stamen"))
        self.assertFalse(self.graph.path_between("Misho", "Stamen"))

    def test_path_between_without_loop_true(self):
        self.graph.add_edge("Ivan", "Georgi")
        self.graph.add_edge("Ivan", "Pesho")
        self.graph.add_edge("Ivan", "Misho")
        self.graph.add_edge("Stamat", "Lubo")
        self.graph.add_edge("Stamat", "Stamen")
        self.graph.add_edge("Georgi", "Stamat")
        self.assertFalse(self.graph.path_between("Ivan", "Stamen"))
        self.assertFalse(self.graph.path_between("Misho", "Stamen"))

    def test_path_between_with_loop_true(self):
        self.graph.add_edge("Ivan", "Georgi")
        self.graph.add_edge("Ivan", "Pesho")
        self.graph.add_edge("Ivan", "Misho")
        self.graph.add_edge("Stamat", "Lubo")
        self.graph.add_edge("Stamat", "Stamen")
        self.graph.add_edge("Georgi", "Stamat")
        self.graph.add_edge("Misho", "Ivan")
        self.assertFalse(self.graph.path_between("Ivan", "Stamen"))
        self.assertFalse(self.graph.path_between("Misho", "Stamen"))


if __name__ == '__main__':
    unittest.main()
