from Parser import *
from TreeSearcher import *

p = Parser()
t = p.fill_tree("gf_output.txt")
p.parser_for_midi(t,3)