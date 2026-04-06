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
    skills: List[Skill]
    education: List[Education]
    experience: List[Experience]
    projects: List[Project]

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    skills: Optional[List[Skill]] = None
    education: Optional[List[Education]] = None
    experience: Optional[List[Experience]] = None
    projects: Optional[List[Project]] = None