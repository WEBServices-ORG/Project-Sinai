from pydantic import BaseModel
from typing import Any

class RunResponse(BaseModel):
    response: Any
