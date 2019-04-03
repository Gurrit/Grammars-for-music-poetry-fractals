import asyncio
import websockets
import json
from Parser import *
import os

fractals = {"Sierpinski", "Dragon", "Koch", "Gosper"}


async def message_receiver (websocket, path):
    async for message in websocket:
        print(message)
        data = json.loads(message)
        map_to_function(data)
        web = parser.parse_for_web(generate_file_name(data))
        for m in web:
            await websocket.send(m)


def map_to_function(data):
    if data['type'] in fractals:
        config.step = data['step']
        if os.path.isfile(generate_file_name(data)):
            return
        else:
            generate_new_fractal_file(data)


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


def generate_file_name(data):
    return config.gf_output_path + data['type'] + str(data['iteration']) + ".txt"


parser = Parser()
asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
