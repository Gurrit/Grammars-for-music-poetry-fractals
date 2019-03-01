import asyncio
import websockets
from config import *
from Parser import *
from turtle import *
import time

async def echo (websocket, path):
    async for message in websocket:
        web = parse_for_web()
        for m in web:
            await websocket.send(m)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '0.0.0.0', config.PORT))
asyncio.get_event_loop().run_forever()
