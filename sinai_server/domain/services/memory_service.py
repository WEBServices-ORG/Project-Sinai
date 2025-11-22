from fastapi import HTTPException
from sinai_server.domain.validation.validators import validate_prompt
from sinai_server.domain.sanitization.sanitizer import sanitize_text

class MemoryService:
    def __init__(self, sinai_core):
        self.core = sinai_core

    async def set_memory(self, ns: str, key: str, value: str) -> dict:
        if not ns or not key:
            raise HTTPException(status_code=400, detail="Namespace and key required")
        validate_prompt(value)
        clean = sanitize_text(value)
        self.core.memory.set(ns, key, clean)
        return {"status": "ok"}

    async def get_memory(self, ns: str, key: str) -> dict:
        if not ns or not key:
            raise HTTPException(status_code=400, detail="Namespace and key required")
        result = self.core.memory.get(ns, key)
        return {"results": result}
