import asyncio
import websockets
import json
from Parser import *
import os
from piano import *
from piano import Piano
import wave, struct
import audioop

fractals = {"Sierpinski", "Dragon", "Koch", "Gosper"}
piano = Piano()


async def message_receiver(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        await map_to_function(websocket, data)




async def map_to_function(websocket, data):
    generate_gf_string(data, fractals)

    if data['mode'] == "piano":
        generate_gf_string(data['type'], data['iteration'])
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

        parser.add_modification_lists(
            piano.colorArray, piano.leftAngleArray, piano.rightAngleArray)
        print("pianoarray: " + str(piano.colorArray))
        web = parser.parse_for_web(generate_file_name(data['type'], data['iteration']))
        message = ""
        for m in web:
            message = data['index'] + ";" + m + "|" + message
            message = message + ("D" + data['index'])
            # print("M??" + message)
        await websocket.send(message)

        # call draw_piano_fractal()
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
        generate_translation(data, websocket)

    if data['mode'] == "music":
        print("inne i musiken")
        name = generate_file_name(data['type'], data['iteration'])
        tree = parser.fill_tree(name)
        make_music(tree, data)

    if data['mode'] == "play":
        print("inne i musiken")
        name = generate_file_name(data['type'], data['iteration'])
        tree = parser.fill_tree(name)
        make_music(tree, data)
        name = str(data['type']) + str(data['iteration'])
        print(str(name))
        filename = ("./wav-files/" + str(name) + ".wav")
        print(str(filename))

        with open(filename, 'rb') as wavefile: #tar tid, ej optimalt för högre grader av iterationer
            contents = wavefile.read()

        print("sending the audio file" + str(contents))
        await websocket.send(contents)


def make_music(tree, data):
    print("skapar musikennnnn")
    parser.parser_for_midi(tree, data)
    os.system("timidity " + generate_midi_name(data) +
              " -Ow -o " + generate_wav_name(data))


def generate_translation(data, websocket):
    generate_gf_string(data, fractals)
    if data['type'] in fractals:
        config.step = data['step']
        if not os.path.isfile(generate_file_name(data['type'], data['iteration'])):
            generate_new_fractal_file(data)
        web = parser.parse_for_web(generate_file_name(data['type'], data['iteration']))
        await websocket.send(create_json("draw", web, 1))


parser = Parser()
asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
