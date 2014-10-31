class Graph():

    def __init__(self):
        self.nodes = {}

    def add_edge(self, nodeA, nodeB):
        if nodeA not in self.nodes:
            self.nodes[nodeA] = [nodeB]
        else:
            paths_arr = self.nodes[nodeA]
            paths_arr.append(nodeB)
        if nodeB not in self.nodes:
            self.nodes[nodeB] = []

    def get_neighbours_for_node(self, node):
        if node not in self.nodes:
            return False
        return self.nodes[node]

    def path_between(self, nodeA, nodeB):
        print(nodeA)
        if len(self.nodes[nodeA]) == 0:
            return False
        if nodeA == nodeB:
            return False
        if nodeA not in self.nodes or nodeB not in self.nodes:
            return False
        if nodeB in self.nodes[nodeA]:
            return True
        for node in self.nodes[nodeA]:
            if self.path_between(node, nodeB):
                return True
        return False


new_graph = Graph()
new_graph.add_edge("Ivan", "Georgi")
new_graph.add_edge("Ivan", "Pesho")
new_graph.add_edge("Ivan", "Misho")

new_graph.add_edge("Stamat", "Lubo")
new_graph.add_edge("Stamat", "Stamen")
# new_graph.add_edge("Georgi", "Stamat")
new_graph.add_edge("Misho", "Ivan")
print(new_graph.path_between("Ivan", "Stamen"))
