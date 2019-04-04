from Parser import *

p = Parser()
p.fill_tree("gf_output.txt").visualise()
p.parser_for_midi()
print(p.tree.depth)

