import asyncio
import websockets
import json
from Parser import *
import os
from piano import *

fractals = {"Sierpinski", "Dragon", "Koch", "Gosper"}


async def message_receiver(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        await map_to_function(websocket, data)


async def map_to_function(websocket, data):
    print(data)
    if data['mode'] == "piano":
        print(data['data'])
        interprete_notes(data['data'])
        print("COLOR" + str(colorArray))
        #go to piano.py
    if data['mode'] == "math":
        pass
        #draw fractal
    if data['mode'] == "draw":
        if data['type'] in fractals:
            config.step = data['step']
            if not os.path.isfile(generate_file_name(data)):
                generate_new_fractal_file(data)
            print("done, sending message")
            web = parser.parse_for_web(generate_file_name(data))
            message = ""
            for m in web:       # Change for speed?
                message = data['index'] + ";" + m + "|" + message
            message = message + ("D" + data['index'])
            await websocket.send(message)


def generate_new_fractal_file(data):
    iteration = data['iteration']
    gf_file = config.gf_file_path + data['type']
    gf_commands = "import " + gf_file + ".gf \n l -bracket c(s "       # How should this look?
    start_iterations = ""
    for i in range(iteration):
        start_iterations = start_iterations + "(s"
    gf_commands = gf_commands + start_iterations + " z)"
    end_iterations = ""
    for i in range(iteration):
        end_iterations = end_iterations + ")"
    gf_commands = gf_commands + end_iterations + " | wf -file=" + generate_file_name(data) + "\n"
    file = open(config.gf_script_path, 'w+')
    file.write(gf_commands)
    file.close()
    print(gf_commands)
    os.system("gf < " + config.gf_script_path)

def make_music(tree, data):
    parser.parser_for_midi(tree, data['iteration'], generate_midi_name(data))
    os.system("timidity " + generate_midi_name(data) + " -Ow -o " + generate_wav_name(data))

def generate_file_name(data):
    return config.gf_output_path + data['type'] + str(data['iteration']) + ".txt"

def generate_midi_name(data):
    return config.midi_path + data['type'] + str(data['iteration']) + ".mid"

def generate_wav_name(data):
    return config.wav_path + data['type'] + str(data['iteration']) + ".wav"


parser = Parser()
asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
