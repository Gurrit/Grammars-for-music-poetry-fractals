def closest_iteration(coordinate, tree, iteration):
    layer = tree.treeLists[iteration]
    closest_line = layer.nodes[0][0].value
    closest_part = 0
    index = 0
    for part in layer.nodes:
        for line in part:
            if line.value.shortest_distance(coordinate) < closest_line.shortest_distance(coordinate):
                closest_part = index
                closest_line = line.value
        index += 1
    return closest_part
