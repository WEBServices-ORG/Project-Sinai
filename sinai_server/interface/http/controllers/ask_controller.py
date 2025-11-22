from sinai_server.domain.services.ask_service import AskService
from sinai_server.core.logging import log_info

class AskController:
    def __init__(self, ask_service: AskService):
        self.service = ask_service

    async def handle(self, query: str, k: int = 5):
        log_info(f"ASK: query len={len(query)}")
        return await self.service.ask(query, k)
