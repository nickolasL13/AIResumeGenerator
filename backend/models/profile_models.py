from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Duration(BaseModel):
    start: date
    end: date

class Experience(BaseModel):
    role: str
    company: str
    description: str
    duration: Duration

class Skill(BaseModel):
    category: str
    name: str
    level: Optional[str] = None

class Skills(BaseModel):
    skills: List[Skill]

class Education(BaseModel):
    degree: str
    institution: str
    finished: bool
    duration: Duration

class Project(BaseModel):
    name: str
    description: str
    link: Optional[str]

class Profile(BaseModel):
    name: str
    email: str
    skills: List[str]
    education: List[Education]
    experience: List[Experience]
    projects: List[Project]