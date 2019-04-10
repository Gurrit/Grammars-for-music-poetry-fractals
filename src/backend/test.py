from Parser import *
from TreeSearcher import *

p = Parser()
t = p.fill_tree()
searcher = TreeSearcher(t)

t.visualise()

print(searcher.closest_iteration(Coordinate(31,31)))