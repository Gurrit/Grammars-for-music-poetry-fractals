
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print("got here")
        await websocket.send("forward(50)")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()