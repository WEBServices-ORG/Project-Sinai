from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sinai_server.core.server_loader import ServerLoader
from sinai_server.interface.http.controllers.agent_controller import AgentController

class AgentRequest(BaseModel):
    task: str = Field(..., min_length=1, max_length=5000)

router = APIRouter(prefix="/agent", tags=["agent"])
loader = ServerLoader()

def get_controller():
    return AgentController(loader.get_container().get_agent_service())

@router.post("/")
async def agent_endpoint(body: AgentRequest, controller: AgentController = Depends(get_controller)):
    return await controller.handle(body.task)
