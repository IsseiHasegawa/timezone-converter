from pydantic import BaseModel
from typing import List, Optional

class ConvertRequest(BaseModel):
    from_timezone: str
    to_timezone: str
    times: List[str]

class ConvertResult(BaseModel):
    input: str
    output: Optional[str] = None
    status: str
    error: Optional[str] = None

