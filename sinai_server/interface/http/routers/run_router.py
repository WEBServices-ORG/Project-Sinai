from fastapi import APIRouter, Depends
from sinai_server.core.server_loader import ServerLoader
from sinai_server.interface.http.controllers.run_controller import RunController
from sinai_server.interface.http.request_models.run_request import RunRequest
from sinai_server.interface.http.response_models.run_response import RunResponse

router = APIRouter(prefix="/run", tags=["run"])
loader = ServerLoader()

def get_controller():
    c = loader.get_container()
    return RunController(c.get_run_service())

@router.post("/", response_model=RunResponse)
async def run_endpoint(body: RunRequest, controller: RunController = Depends(get_controller)):
    return RunResponse(**(await controller.handle(body.prompt)))
