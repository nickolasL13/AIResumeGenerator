from pydantic import BaseModel
from typing import List
from models.profile_models import Profile

class Resume(BaseModel):
    summary: str
    profile: Profile
    
