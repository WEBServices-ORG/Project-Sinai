from sinai_server.domain.validation.validators import validate_prompt
from sinai_server.domain.sanitization.sanitizer import sanitize_text

class AskService:
    def __init__(self, sinai_core):
        self.core = sinai_core

    async def ask(self, query: str, k: int = 5) -> dict:
        validate_prompt(query)
        clean = sanitize_text(query)
        result = self.core.ask(clean, k)
        return {"results": result}
