from Parser import *

p = Parser()
p.fill_tree().visualise()
p.parser_for_midi()
print(p.tree.depth)