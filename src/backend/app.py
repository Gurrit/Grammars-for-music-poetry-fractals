import asyncio
import websockets
from config import *
import json
from Parser import *
from turtle import *
import time
import subprocess
import os

fractals = {"Sierpinski", "Dragon", "Koch", "Gosper"}


async def message_receiver (websocket, path):
    async for message in websocket:
        print(message)
        data = json.loads(message)
        map_to_function(data)
    #    web = parse_for_web()
    #    for m in web:
    #        await websocket.send(m)


def map_to_function(data):
    if data['type'] in fractals:
        gf_file = config.gf_file_path + data['type']
        gf_commands = "import " + gf_file + ".gf \n" \
                      "l s (s (s z)) | wf -file=" + config.gf_output_path + "\n"    # This should not be hardcoded.
        file = open(config.gf_script_path, 'w+')
        file.write(gf_commands)
        file.close()
        os.system("gf < " + config.gf_script_path)



asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
