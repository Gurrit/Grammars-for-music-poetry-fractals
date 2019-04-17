from Parser import *
from TreeSearcher import *
#from app import *

p = Parser()
t = p.fill_tree("gf_output.txt")
data = {'iteration':"1", 'type':"Gosper"}

def make_music(tree, data):
    p.parser_for_midi(tree, int(data['iteration']), generate_midi_name(data))
    os.system("timidity " + generate_midi_name(data) + " -Ow -o " + generate_wav_name(data))

def generate_midi_name(data):
    return config.midi_path + data['type'] + str(data['iteration']) + ".mid"

def generate_wav_name(data):
    return config.wav_path + data['type'] + str(data['iteration']) + ".wav"

make_music(t,data)