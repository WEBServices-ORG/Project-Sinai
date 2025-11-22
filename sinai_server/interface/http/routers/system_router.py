from fastapi import APIRouter, Depends
from sinai_server.core.server_loader import ServerLoader
from sinai_server.domain.services.system_service import SystemService

router = APIRouter(prefix="/system", tags=["system"])
loader = ServerLoader()

def get_system_service():
    return loader.get_container().get_system_service()

@router.get("/health")
async def system_health(svc: SystemService = Depends(get_system_service)):
    return await svc.health()

@router.get("/info")
async def system_info(svc: SystemService = Depends(get_system_service)):
    return await svc.system_info()
