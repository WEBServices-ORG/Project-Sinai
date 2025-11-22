import os
from fastapi import HTTPException
from sinai_server.domain.validation.validators import validate_prompt
from sinai_server.domain.sanitization.sanitizer import sanitize_text

class RAGService:
    def __init__(self, sinai_core):
        self.core = sinai_core

    async def ingest(self, folder_path: str) -> dict:
        if not folder_path:
            raise HTTPException(status_code=400, detail="Folder path required")
        folder_path = folder_path.strip()
        if not os.path.exists(folder_path):
            raise HTTPException(status_code=404, detail="Folder not found")
        result = self.core.ingest(folder_path)
        return {"ingest": result}

    async def ask(self, query: str, k: int = 5) -> dict:
        validate_prompt(query)
        clean_query = sanitize_text(query)
        result = self.core.ask(clean_query, k)
        return {"results": result}
