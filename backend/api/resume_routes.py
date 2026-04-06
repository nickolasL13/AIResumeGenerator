from fastapi import APIRouter, HTTPException
import storage.json_storage as storage
from models.job_models import JobDescription
from services.resume_service import generate_resume_service

router = APIRouter()

@router.post("/resume/generate")
def generate_resume(job_description: JobDescription):
    profile = storage.load_profile()
    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found. Create a profile first."
        )

    result = generate_resume_service(profile, job_description)

    metadata = storage.save_resume(job_description.job_description, result)

    return {
        "message": "Resume generated successfully",
        "resume": result,
        "filename": metadata["filename"]
    }

@router.get("/resumes")
def list_resumes():
    resumes = storage.list_resumes()
    return {"resumes": resumes}

@router.get("/resume/{filename}")
def get_resume(filename: str):
    content = storage.load_resume(filename)
    if content is None:
        raise HTTPException(status_code=404, detail="Resume not found")
    return {"filename": filename, "content": content}
