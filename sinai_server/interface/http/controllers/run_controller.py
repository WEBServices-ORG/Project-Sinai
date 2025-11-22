from sinai_server.domain.services.run_service import RunService
from sinai_server.core.logging import log_info

class RunController:
    def __init__(self, run_service: RunService):
        self.service = run_service

    async def handle(self, prompt: str):
        log_info(f"RUN: prompt len={len(prompt)}")
        return await self.service.run(prompt)
