from sinai_server.domain.validation.validators import validate_prompt
from sinai_server.domain.sanitization.sanitizer import sanitize_text

class RunService:
    def __init__(self, sinai_core):
        self.core = sinai_core

    async def run(self, prompt: str) -> dict:
        validate_prompt(prompt)
        clean = sanitize_text(prompt)
        result = self.core.run(clean)
        return {"response": result}
