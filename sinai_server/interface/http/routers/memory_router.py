from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sinai_server.core.server_loader import ServerLoader
from sinai_server.domain.services.memory_service import MemoryService

class MemorySetRequest(BaseModel):
    ns: str
    key: str
    value: str

class MemoryGetRequest(BaseModel):
    ns: str
    key: str

router = APIRouter(prefix="/memory", tags=["memory"])
loader = ServerLoader()

def get_memory_service():
    return loader.get_container().get_memory_service()

@router.post("/set")
async def memory_set(body: MemorySetRequest, svc: MemoryService = Depends(get_memory_service)):
    return await svc.set_memory(body.ns, body.key, body.value)

@router.post("/get")
async def memory_get(body: MemoryGetRequest, svc: MemoryService = Depends(get_memory_service)):
    return await svc.get_memory(body.ns, body.key)
