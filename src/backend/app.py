import asyncio
import base64

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
    if data['mode'] == "piano":
        await generate_piano_fractal(data, websocket)
    if data['mode'] == "coordinate":
        await generate_translation(data, websocket)
    if data['mode'] == "draw":
        await generate_fractal(data, websocket)
    if data['mode'] == "play":
        await generate_music_file(data, websocket)


def make_music(tree, data): # this should probably be moved.
    print("skapar musikennnnn")
    parser.parser_for_midi(tree, data)
    os.system("timidity " + generate_midi_name(data) +
              " -Ow -o " + generate_wav_name(data))


async def generate_music_file(data, websocket):
    filename = generate_file_name(data['type'], data['iteration'])
    tree = parser.fill_tree(filename)
    make_music(tree, data)
    name = str(data['type']) + str(data['iteration'])
    filename = ("./wav-files/" + str(name) + ".wav")
    with open(filename, 'rb') as wavefile:  # tar tid, ej optimalt för högre grader av iterationer
        contents = wavefile.read()
    await websocket.send(contents)


async def generate_fractal(data, websocket):
    generate_gf_string(data, fractals)
    if data['type'] in fractals:
        config.step = data['step']
        if not os.path.isfile(generate_file_name(data['type'], data['iteration'])):
            generate_new_fractal_file(data)
        web = parser.parse_for_web((data['type']) + str(data['iteration']),
                                   generate_file_name(data['type'], str(data['iteration'])), False)
        await websocket.send(create_draw_json(web, data['index'], data['type'], data['iteration']))


async def generate_piano_fractal(data, websocket):      # This should probably have code moved.
    generate_gf_string(data, fractals)
    angle = 0
    # Get the angle from the GF-file and send it to the piano-interpreter
    file_reader = GFFileReader()
    commands = file_reader.read_gf_file(generate_file_name(data['type'], data['iteration']))
    config.step = data['step']
    if "ang" in commands[1]:
        angle = int(commands[1].split(":")[1])
    piano.reset_drawing_arrays()
    piano.interpret_notes(data['data'], angle)
    parser.add_modification_lists(
        piano.colorArray, piano.leftAngleArray, piano.rightAngleArray)
    web = parser.parse_for_web((data['type']) + str(data['iteration']) + "_modified",
                               generate_file_name(data['type'], str(data['iteration'])),  True)
    await websocket.send(create_draw_json(web, data['index'], data['type'], data['iteration']))


async def generate_translation(data, websocket):
    lines = parser.find_iteration((data['type']) + str(data['iteration'] + "_modified"), data['coordinate'],
                                  (data['to']) + str(data['iteration'] + "_modified"))
    await websocket.send(create_translation_json(lines))


parser = Parser()
asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
