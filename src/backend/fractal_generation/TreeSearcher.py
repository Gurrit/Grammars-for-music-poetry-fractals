class TreeSearcher:
    def __init__(self, tree):
        self.tree = tree

    def closest_iteration(self, coordinate):
        closest_layer = self.tree.treeLists[0]
        closest_line = self.tree.treeLists[0].nodes[0].value
        for layer in self.tree.treeLists:
            for node in layer.nodes:
                if node.value.shortest_distance(coordinate) < closest_line.shortest_distance(coordinate):
                    closest_layer = layer
                    closest_line = node.value

        return closest_layer
