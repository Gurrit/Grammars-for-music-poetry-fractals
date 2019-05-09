from Config import *


def generate_file_name(type, iteration):
    return Config.gf_output_path + type + str(iteration) + ".txt"


def generate_midi_name(data):
    return Config.midi_path + data['type'] + str(data['iteration']) + ".mid"


def generate_wav_name(data):
    return Config.wav_path + data['type'] + str(data['iteration']) + ".wav"


def generate_new_fractal_file(data):
    iteration = data['iteration']
    gf_file = Config.gf_file_path + data['type']
    gf_commands = "import " + gf_file + \
                  ".gf \n l -bracket c( "  # How should this look?
    start_iterations = ""
    for i in range(iteration):
        start_iterations = start_iterations + "s("
    gf_commands = gf_commands + start_iterations + " z)"
    end_iterations = ""
    for i in range(iteration):
        end_iterations = end_iterations + ")"
    gf_commands = gf_commands + end_iterations + \
                  " | wf -file=" + generate_file_name(data['type'], data['iteration']) + "\n"
    file = open(Config.gf_script_path, 'w+')
    file.write(gf_commands)
    file.close()
    print("GF commands: " + str(gf_commands))
    os.system("gf < " + Config.gf_script_path)


def generate_gf_string(data, fractals):
    if data['type'] in fractals:
        Config.step = data['step']
        if not os.path.isfile(generate_file_name(data['type'], data['iteration'])):
            generate_new_fractal_file(data)
