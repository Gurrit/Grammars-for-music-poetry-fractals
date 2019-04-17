from config import *

def generate_file_name(data):
    return config.gf_output_path + data['type'] + str(data['iteration']) + ".txt"


def generate_midi_name(data):
    return config.midi_path + data['type'] + str(data['iteration']) + ".mid"


def generate_wav_name(data):
    print("skapar wav-filen")
    return config.wav_path + data['type'] + str(data['iteration']) + ".wav"


def generate_new_fractal_file(data):
    iteration = data['iteration']
    gf_file = config.gf_file_path + data['type']
    gf_commands = "import " + gf_file + \
        ".gf \n l -bracket c(s "       # How should this look?
    start_iterations = ""
    for i in range(iteration):
        start_iterations = start_iterations + "(s"
    gf_commands = gf_commands + start_iterations + " z)"
    end_iterations = ""
    for i in range(iteration):
        end_iterations = end_iterations + ")"
    gf_commands = gf_commands + end_iterations + \
        " | wf -file=" + generate_file_name(data) + "\n"
    file = open(config.gf_script_path, 'w+')
    file.write(gf_commands)
    file.close()
    print("GF commands: " + str(gf_commands))
    os.system("gf < " + config.gf_script_path)


def generate_gf_string(data, fractals):
    if data['type'] in fractals:
        config.step = data['step']
        if not os.path.isfile(generate_file_name(data)):
            generate_new_fractal_file(data)
        print("done, sending message")