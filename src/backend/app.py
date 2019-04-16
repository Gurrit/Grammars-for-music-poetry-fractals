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
        if not os.path.isfile(generate_file_name(data)):
            generate_new_fractal_file(data)
        print("done, sending message")

async def map_to_function(websocket, data):
    generate_gf_string(data)
    print(data)

    if data['mode'] == "piano":
        angle = 0
        print(data['data'])

        # Get the angle from the GF-file and send it to the piano-interpreter
        file_reader = GFFileReader()
        commands = file_reader.read_gf_file(generate_file_name(data))
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
        web = parser.parse_for_web(generate_file_name(data))


        message = ""
        for m in web:
            message = data['index'] + ";" + m + "|" + message
            message = message + ("D" + data['index'])
            # print("M??" + message)
        await websocket.send(message)

        #call draw_piano_fractal()
    if data['mode'] == "draw":
        if data['type'] in fractals:
            config.step = data['step']
            print(str(config.step))
            if not os.path.isfile(generate_file_name(data)):
                generate_new_fractal_file(data)
            print("done, sending message")
            web = parser.parse_for_web(generate_file_name(data))
            message = ""
            for m in web:  # Change for speed?
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
    print("GF commands: " + str(gf_commands))
    os.system("gf < " + config.gf_script_path)


def generate_file_name(data):
    return config.gf_output_path + data['type'] + str(data['iteration']) + ".txt"


parser = Parser()
asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
