def closest_iteration(coordinate, tree):
    closest_layer = tree.treeLists[0]
    closest_line = tree.treeLists[0].nodes[0].value
    for layer in tree.treeLists:
        for node in layer.nodes:
            if node.value.shortest_distance(coordinate) < closest_line.shortest_distance(coordinate):
                closest_layer = layer
                closest_line = node.value
    return closest_layer
