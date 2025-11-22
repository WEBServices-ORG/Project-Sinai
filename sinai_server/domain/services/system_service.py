import platform, time

class SystemService:
    def __init__(self, sinai_core):
        self.core = sinai_core

    async def health(self) -> dict:
        return {"status": "ok", "time": time.time()}

    async def system_info(self) -> dict:
        return {
            "platform": platform.system(),
            "release": platform.release(),
            "python_version": platform.python_version(),
        }
