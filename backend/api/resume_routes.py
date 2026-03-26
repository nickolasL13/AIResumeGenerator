from fastapi import APIRouter
import storage.json_storage as storage
from models.profile_models import Profile
from models.job_models import JobDescription
from services.resume_service import generate_resume_service

router = APIRouter()

@router.post("/resume/generate")
def generate_reseume(profile: Profile, job_description: JobDescription):
    
    resume = generate_resume_service(profile, job_description)

    return {
    "message": "Profile succesfuly created",
    "resume": resume
    }
