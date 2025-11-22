from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sinai_server.core.server_loader import ServerLoader
from sinai_server.interface.http.controllers.ask_controller import AskController


class AskRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=5000)
    k: int = 5


router = APIRouter(prefix="/ask", tags=["ask"])
loader = ServerLoader()


def get_controller():
    return AskController(loader.get_container().get_ask_service())


@router.post("/")
async def ask_endpoint(
    body: AskRequest, controller: AskController = Depends(get_controller)
):
    return await controller.handle(body.query, body.k)


@router.post("/question")
async def ask_question_endpoint(
    body: AskRequest, controller: AskController = Depends(get_controller)
):
    return await controller.handle(body.query, body.k)
