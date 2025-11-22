from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from sinai_server.core.server_loader import ServerLoader
from sinai_server.core.error_handler import register_error_handlers
from sinai_server.core.logging import init_logging, log_info
from sinai_server.core.rate_limit import TokenBucket

from sinai_server.interface.http.routers.run_router import router as run_router
from sinai_server.interface.http.routers.ask_router import router as ask_router
from sinai_server.interface.http.routers.agent_router import router as agent_router
from sinai_server.interface.http.routers.rag_router import router as rag_router
from sinai_server.interface.http.routers.memory_router import router as memory_router
from sinai_server.interface.http.routers.system_router import router as system_router
from sinai_server.interface.http.routers.ask_router import router as ask_router_v1

from sinai_server.interface.ws.sockets.event_stream import event_stream_endpoint

app = FastAPI(
    title="Project Sinai Server",
    version="1.0.0",
    description="Project Sinai – Secure Server Layer",
)

init_logging()
log_info("Sinai Server Booting...")

loader = ServerLoader()
container = loader.get_container()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

global_bucket = TokenBucket(capacity=30, refill_rate=10)

app.include_router(run_router, prefix="/api/sinai")
app.include_router(ask_router, prefix="/api/sinai")
app.include_router(agent_router, prefix="/api/sinai")
app.include_router(rag_router, prefix="/api/sinai")
app.include_router(memory_router, prefix="/api/sinai")
app.include_router(system_router, prefix="/api/sinai")
app.include_router(ask_router_v1, prefix="/api/v1/ai")

app.mount("/", StaticFiles(directory="ui/web/dist", html=True), name="static")


@app.websocket("/api/sinai/events")
async def events_ws(websocket):
    await event_stream_endpoint(websocket)


register_error_handlers(app)


@app.get("/api/health")
def root():
    log_info("Health check OK")
    return {"status": "ok", "server": "project_sinai"}


log_info("Sinai Server Ready.")
