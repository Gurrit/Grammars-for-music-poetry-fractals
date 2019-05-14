import asyncio

import websockets

from Parser import *
from fractal_generation.Piano import Piano
from utils.GFFileReader import *
from utils.SerializeUtils import *

fractals = {"Sierpinski", "Dragon", "Koch", "Gosper"}
piano = Piano()


async def message_receiver(websocket, path):  # path needed to match documentation
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


def make_music(tree, data):  # this should probably be moved.
    parser.parser_for_midi(tree, data)
    os.system("timidity " + generate_midi_name(data) +
              " -Ow -o " + generate_wav_name(data))


async def generate_music_file(data, websocket):
    filename = generate_file_name(data['type'], data['iteration'])
    tree = parser.fill_tree(filename)
    make_music(tree, data)
    name = generate_wav_name(data)
    with open(name, 'rb') as wav_file:  # tar tid, ej optimalt för högre grader av iterationer
        contents = wav_file.read()
    await websocket.send(contents)


async def generate_fractal(data, websocket):
    generate_gf_string(data, fractals)
    if data['type'] in fractals:
        Config.step = data['step']
        if not os.path.isfile(generate_file_name(data['type'], data['iteration'])):
            generate_new_fractal_file(data)
        web = parser.parse_for_web((data['type']) + str(data['iteration']),
                                   generate_file_name(data['type'], str(data['iteration'])), False)
        await websocket.send(create_draw_json(web, data['index'], data['type'], data['iteration'], False))


async def generate_piano_fractal(data, websocket):  # This should probably have code moved.
    generate_gf_string(data, fractals)
    angle = 0
    # Get the angle from the GF-file and send it to the piano-interpreter
    commands = read_gf_file(generate_file_name(data['type'], data['iteration']))
    Config.step = data['step']
    if "ang" in commands[1]:
        angle = int(commands[1].split(":")[1])
    piano.reset_drawing_arrays()
    piano.interpret_notes(data['data'], angle)
    parser.add_modification_lists(
        piano.colorArray, piano.leftAngleArray, piano.rightAngleArray)
    web = parser.parse_for_web((data['type']) + str(data['iteration']) + "_modified",
                               generate_file_name(data['type'], str(data['iteration'])), True)
    await websocket.send(create_draw_json(web, data['index'], data['type'], data['iteration'], True))


async def generate_translation(data, websocket):
    modifed = ""
    if data['modified']:
        modifed = "_modified"
    [to_lines, from_lines] = parser.find_iteration((data['type']) + str(data['iteration']) + modifed, data['coordinate'],
                                                   data['to'] + str(data['iteration']) + modifed, data['translation_iteration'])
    await websocket.send(create_translation_json(to_lines, 1))
    await websocket.send(create_translation_json(from_lines, 0))


parser = Parser()
asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', Config.PORT))
asyncio.get_event_loop().run_forever()
