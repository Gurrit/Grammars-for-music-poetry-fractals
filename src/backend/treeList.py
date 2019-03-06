class TreeList:

    def __init__(self):
        self.__treeLists = []
        self.__depth = 0

    def add_new_layer(self):
        self.__treeLists.append([])
        self.__depth += 1






class TreeListInternal:

    def __init__(self, objects):
        self.objects = objects   # Better name?





class ObjectWrapper:

    def __init__(self, value, parrent):
        self.__value = value
        self.__parrent = parrent
        self.__children = []

