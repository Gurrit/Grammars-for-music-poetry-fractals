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

        parser.add_modification_lists(
            piano.colorArray, piano.leftAngleArray, piano.rightAngleArray)
        print("pianoarray: " + str(piano.colorArray))
        web = parser.parse_for_web(generate_file_name(data))
        message = ""
        for m in web:
            message = data['index'] + ";" + m + "|" + message
        message = message + ("D" + data['index'])
        print("M??" + message)
        await websocket.send(message)

        # call draw_piano_fractal()
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

    if data['mode'] == "music":
        print("inne i musiken")
        name = generate_file_name(data)
        tree = parser.fill_tree(name)
        make_music(tree, data)

    if data['mode'] == "play":
        print("inne i musiken")
        name = generate_file_name(data)
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




parser = Parser()
asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
