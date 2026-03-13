from fastapi import APIRouter
import storage.json_storage as storage
from models.profile_models import Profile

router = APIRouter()

@router.get("/profile")
def get_profile():
    return {
        "message": "Profile successfuly retrieved",
        "profile": storage.load_profile()
        }

@router.post("/profile")
def create_profile(profile: Profile):
    storage.save_profile(profile)
    return {
    "message": "Profile created",
    "profile": profile.model_dump()
    }

