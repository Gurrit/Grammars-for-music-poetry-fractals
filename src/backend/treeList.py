class TreeList:

    def __init__(self):
        self.__treeLists = []
        self.__depth = 0

    def add_new_iteration(self):
        layer = Layer()
        self.__treeLists.append(layer)
        self.__depth += 1
        return layer

    def get_layer(self, layer):
        if layer > self.__depth:
            raise IndexError("the structure is not that deep")
        return self.__treeLists[layer]

    def get_depth(self):
        return self.__depth

    def remove_structure(self):
        for list in self.__treeLists:
            list.remove_all_nodes()
        self.__treeLists = []
        self.__depth = 0


class Layer:

    def __init__(self):
        self.__nodes = []  # Better name?

    def append(self, node):
        list.append(self.__nodes, node)

    def get_nodes(self):
        return self.__nodes

    def remove_all_nodes(self):
        for n in self.__nodes:
            self.remove_node(n)
        self.__nodes = []

    def remove_node(self, node):
        list.remove(self.__nodes, node)
        node.remove_parrent()
        node.remove_all_children()



class Node:

    def __init__(self, value, parent):
        self.__value = value
        self.__parent = parent
        self.__children = []
        if parent is not None:
            parent.add_child(self)

    def get_value(self):
        return self.__value

    def get_parent(self):
        return self.__parent

    def add_child(self, child):
        self.__children.append(child)

    def get_children(self):
        return self.__children

    def remove_parent(self):
        self.__parent.remove_child(self)
        self.__parent = None

    def remove_child(self, child):
        self.__children.remove(child)

    def remove_all_children(self):
        for child in self.__children:
            child.remove_parrent()
        self.__children = []

