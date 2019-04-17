import asyncio
import websockets
import json
from Parser import *
import os
from piano import *
from piano import Piano

fractals = {"Sierpinski", "Dragon", "Koch", "Gosper"}
piano = Piano()


async def message_receiver (websocket, path):
    async for message in websocket:
        data = json.loads(message)
        await map_to_function(websocket, data)


def generate_gf_string(data):
    if data['type'] in fractals:
        config.step = data['step']
        if not os.path.isfile(generate_file_name(data['type'], data['iteration'])):
            generate_new_fractal_file(data)


async def map_to_function(websocket, data):
    print(data)

    if data['mode'] == "piano":
        generate_gf_string(data)
        angle = 0
        print(data['data'])

        # Get the angle from the GF-file and send it to the piano-interpreter
        file_reader = GFFileReader()
        commands = file_reader.read_gf_file(generate_file_name(data['type'], data['iteration']))
        config.step = data['step']

        print("READ FILE")
        if "ang" in commands[1]:
            angle = int(commands[1].split(":")[1])

        piano.reset_drawing_arrays()
        piano.interpret_notes(data['data'], angle)

        print("COLOR" + str(piano.colorArray))
        print("RIGHT ANGLE" + str(piano.rightAngleArray))
        print("LEFT ANGLE" + str(piano.leftAngleArray))

        parser.add_modification_lists(piano.colorArray, piano.leftAngleArray, piano.rightAngleArray)
        print("pianoarray: " + str(piano.colorArray))
        print("innan web?")
        web = parser.parse_for_web(generate_file_name(data['type'], data['iteration']))
        print("efter web?")
        message = ""
        for m in web:
            message = data['index'] + ";" + m + "|" + message
        message = message + ("D" + data['index'])
        print("M??" + message)
        await websocket.send(message)

        #call draw_piano_fractal()
        #go to piano.py
    if data['mode'] == "math":
        pass
        #draw fractal
    if data['mode'] == "coordinate":
        toFractal = data['to']
        lines = parser.find_iteration(generate_file_name(data['type'], data['iteration']), data['coordinate'],
                                      generate_file_name(data['to'], data['iteration']))
        message = ""
        for m in lines:
            message = "1" + ";" + m + "|" + message
        message = message + ("+" + "1" + "&" + data['type'] + "*" + str(data['iteration']))
        await websocket.send(message)

    if data['mode'] == "draw":
        generate_gf_string(data)
        if data['type'] in fractals:
            config.step = data['step']
            print(str(config.step))
            if not os.path.isfile(generate_file_name(data['type'], data['iteration'])):
                generate_new_fractal_file(data)
            print("done, sending message")
            web = parser.parse_for_web(generate_file_name(data['type'], data['iteration']))
            message = ""
            for m in web:       # Why did I do this?
                message = data['index'] + ";" + m + "|" + message
            message = message + ("+" + data['index'] + "&" + data['type'] + "*" + str(data['iteration']))
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
    gf_commands = gf_commands + end_iterations + " | wf -file=" + generate_file_name(data['type'], data['iteration']) + "\n"
    file = open(config.gf_script_path, 'w+')
    file.write(gf_commands)
    file.close()
    print("GF commands: " + str(gf_commands))
    os.system("gf < " + config.gf_script_path)


def generate_file_name(frac_type, iteration):
    return config.gf_output_path + frac_type + str(iteration) + ".txt"


parser = Parser()
asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
