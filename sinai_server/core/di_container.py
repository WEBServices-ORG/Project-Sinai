from typing import Optional
from sinai_core.api.sinai import Sinai
from sinai_server.domain.services.ask_service import AskService


class DIContainer:
    def __init__(self):
        self._sinai_core_instance: Optional[Sinai] = None
        self._ask_service_instance: Optional[AskService] = None

    @property
    def sinai_core(self) -> Sinai:
        if self._sinai_core_instance is None:
            self._sinai_core_instance = Sinai()
        return self._sinai_core_instance

    def get_ask_service(self) -> AskService:
        if self._ask_service_instance is None:
            self._ask_service_instance = AskService(self.sinai_core)
        return self._ask_service_instance
