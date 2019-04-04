class TreeList:

    def __init__(self):
        self.treeLists = []
        self.depth = 0

    def add_new_iteration(self, amount=1):
        for i in range(amount):
            layer = Layer()
            self.treeLists.append(layer)
            self.depth += 1

    def get_layer(self, layer):
        if layer > self.depth-1:
            raise IndexError("the structure is not that deep")
        return self.treeLists[layer]


    def remove_structure(self):
        for list in self.treeLists:
            list.remove_all_nodes()
        self.treeLists = []
        self.depth = 0

    def visualise(self):
        for layer in self.treeLists:
            print(layer.to_string())



class Layer:

    def __init__(self):
        self.nodes = []  # Better name?

    def append(self, node):
        list.append(self.nodes, node)

    def remove_all_nodes(self):
        for n in self.nodes:
            self.remove_node(n)
        self.nodes = []

    def remove_node(self, node):
        list.remove(self.nodes, node)
        node.remove_parrent()
        node.remove_all_children()

    def to_string(self):
        if len(self.nodes) != 0:
            s = "[(" + str(self.nodes[0].value.coordinate_1.x) + ", " + str(self.nodes[0].value.coordinate_1.y) + ")"
            for node in self.nodes:
                s += ", (" + str(node.value.coordinate_2.x) + ", " + str(node.value.coordinate_2.y) + ")"
            s += "]"
            return s
        return None



class Node:

    def __init__(self, value, children=None):
        if children is None:
            children = []
        self.value = value
        self.parent = None
        self.children = children
        for child in children:
            child.add_parent(self)

    def add_child(self, child):
        self.children.append(child)

    def remove_parent(self):
        self.parent.remove_child(self)
        self.parent = None

    def add_parent(self, parent):
        self.parent = parent

    def remove_child(self, child):
        self.children.remove(child)

    def remove_all_children(self):
        for child in self.children:
            child.remove_parrent()
        self.children = []