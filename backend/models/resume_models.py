from pydantic import BaseModel
from typing import List

class Resume(BaseModel):
    summary: str
    experience: List[str]
    skills: List[str]