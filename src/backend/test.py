from Parser import *
from TreeSearcher import *

p = Parser()
t = p.fill_tree()
searcher = TreeSearcher(t)

t.visualise()

print(searcher.closest_iteration(coordinate(31,31)))