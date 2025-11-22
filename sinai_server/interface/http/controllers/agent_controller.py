from sinai_server.domain.services.agent_service import AgentService
from sinai_server.core.logging import log_info

class AgentController:
    def __init__(self, agent_service: AgentService):
        self.service = agent_service

    async def handle(self, task: str):
        log_info(f"AGENT: task len={len(task)}")
        return await self.service.run_agent(task)
