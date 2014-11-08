class DirectedGraph():

    checked_nodes = []

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
        DirectedGraph.checked_nodes.append(nodeA)
        if len(self.nodes[nodeA]) == 0:
            return False
        elif nodeA == nodeB:
            return False
        elif nodeA not in self.nodes or nodeB not in self.nodes:
            return False
        elif nodeB in self.nodes[nodeA]:
            return True
        for node in self.nodes[nodeA]:
            if node in DirectedGraph.checked_nodes:
                return False
            if self.path_between(node, nodeB):
                return True
        return False

    def __str__(self):
        print(self.nodes)
