import asyncio
import websockets
from config import *
import json
from Parser import *
from turtle import *
import time

fractals = {"sierpinski", "dragon", "koch", "gosper"}


class Message:
    hej = []


async def message_receiver (websocket, path):
    async for message in websocket:
        data = json.loads(message)
        map_to_function(data)
        web = parse_for_web()
        for m in web:
            await websocket.send(m)


def map_to_function(data):
    if data['type'] in fractals:
        


asyncio.get_event_loop().run_until_complete(
    websockets.serve(message_receiver, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
