import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        print("got here")
        await websocket.send("forward(50)")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '0.0.0.0', ))
asyncio.get_event_loop().run_forever()
