from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sinai_server.core.server_loader import ServerLoader
from sinai_server.domain.services.rag_service import RAGService

class RAGIngestRequest(BaseModel):
    folder_path: str

class RAGAskRequest(BaseModel):
    query: str = Field(..., min_length=1)
    k: int = 5

router = APIRouter(prefix="/rag", tags=["rag"])
loader = ServerLoader()

def get_rag_service():
    return loader.get_container().get_rag_service()

@router.post("/ingest")
async def rag_ingest(body: RAGIngestRequest, svc: RAGService = Depends(get_rag_service)):
    return await svc.ingest(body.folder_path)

@router.post("/ask")
async def rag_ask(body: RAGAskRequest, svc: RAGService = Depends(get_rag_service)):
    return await svc.ask(body.query, body.k)
