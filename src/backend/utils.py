import json

from config import *

def generate_file_name(type, iteration):
    return config.gf_output_path + type + str(iteration) + ".txt"


def generate_midi_name(data):
    return config.midi_path + data['type'] + str(data['iteration']) + ".mid"


def generate_wav_name(data):
    print("skapar wav-filen")
    return config.wav_path + data['type'] + str(data['iteration']) + ".wav"


def generate_new_fractal_file(data):
    iteration = data['iteration']
    gf_file = config.gf_file_path + data['type']
    gf_commands = "import " + gf_file + \
        ".gf \n l -bracket c( "       # How should this look?
    start_iterations = ""
    for i in range(iteration):
        start_iterations = start_iterations + "s("
    gf_commands = gf_commands + start_iterations + " z)"
    end_iterations = ""
    for i in range(iteration):
        end_iterations = end_iterations + ")"
    gf_commands = gf_commands + end_iterations + \
        " | wf -file=" + generate_file_name(data['type'], data['iteration']) + "\n"
    file = open(config.gf_script_path, 'w+')
    file.write(gf_commands)
    file.close()
    print("GF commands: " + str(gf_commands))
    os.system("gf < " + config.gf_script_path)


def generate_gf_string(data, fractals):
    if data['type'] in fractals:
        config.step = data['step']
        if not os.path.isfile(generate_file_name(data['type'], data['iteration'])):
            generate_new_fractal_file(data)


def serialize_coords(coordinate):
    return {'x': coordinate.x, 'y': coordinate.y}


def create_draw_json(lines, canvas, fractal, iteration):
    # Is not serialized, since Python is weird when it comes to serializing
    ser_val = json.dumps({'mode': "draw",
                           'lines': [{'coordinate1': serialize_coords(i.coordinate_1),
                                      'coordinate2': serialize_coords(i.coordinate_2),
                                      'color': i.color
                                      }for i in lines],
                            'canvas': canvas,
                            'type': fractal,
                            'iteration': iteration}, sort_keys=True, indent=2, separators=(',', ': '))
    # List comprehension, effective way of getting all coords and color in one loop.

    return ser_val


def create_music_json(file):
    ser_val = json.dumps({'mode': "music", 'content': file}, sort_keys=True, indent=2, separators=(',', ': '))
    return ser_val


def create_translation_json(lines):
    ser_val = json.dumps({'mode': "translation",
                          'lines': [{'coordinate1': serialize_coords(i.coordinate_1),
                                      'coordinate2': serialize_coords(i.coordinate_2),
                                      'color': i.color
                                      }for i in lines]}, sort_keys=True, indent=2, separators=(',', ': '))
    return ser_val

