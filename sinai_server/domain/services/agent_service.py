from sinai_server.domain.validation.validators import validate_prompt
from sinai_server.domain.sanitization.sanitizer import sanitize_text

class AgentService:
    def __init__(self, sinai_core):
        self.core = sinai_core

    async def run_agent(self, task: str) -> dict:
        validate_prompt(task)
        clean = sanitize_text(task)
        result = self.core.think(clean)
        return {"agent": result}
