from Parser import *

p = Parser()
t = p.fill_tree("gf_output.txt")

#for node in t.get_layer(5).nodes:
    #v = node.value
    #print("(" + str(v.coordinate_1.x) + "," + str(v.coordinate_1.y) + ") to (" + str(v.coordinate_2.x) + "," + str(v.coordinate_2.y) + ") , angle: " + str(v.angle))
    #print("(" + str(v.x_length) + "," + str(v.y_length) + "), angle: " + str(v.angle))

p.parser_for_midi()




