from fastapi import WebSocket, WebSocketDisconnect
from sinai_server.core.server_loader import ServerLoader
from sinai_server.core.logging import log_info

loader = ServerLoader()

class EventStreamSocket:
    def __init__(self, websocket: WebSocket):
        self.ws = websocket
        self.container = loader.get_container()
        self.core = self.container.sinai_core

    async def connect(self):
        await self.ws.accept()
        log_info("WS client connected")

    async def disconnect(self):
        log_info("WS client disconnected")

    async def send_event(self, event: str, payload: dict):
        await self.ws.send_json({"event": event, "data": payload})

async def event_stream_endpoint(websocket: WebSocket):
    socket = EventStreamSocket(websocket)
    await socket.connect()

    bus = socket.core.events

    async def callback(payload):
        await socket.send_event("event", payload or {})

    bus.subscribe("system", callback)
    bus.subscribe("agent", callback)
    bus.subscribe("rag", callback)
    bus.subscribe("log", callback)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await socket.disconnect()
