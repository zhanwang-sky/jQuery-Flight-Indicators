#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# WS server that sends messages at fixed interval

import asyncio
import math
import websockets

async def time(websocket, path):
    inc = 0
    while True:
        #now = datetime.datetime.utcnow().isoformat() + 'Z'
        pitch = 24 * math.sin(inc / 100)
        roll = 180 * math.sin(inc / 70)
        await websocket.send(str(pitch) + ' ' + str(roll))
        await asyncio.sleep(0.02)
        inc += 1

start_server = websockets.serve(time, '', 9000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
