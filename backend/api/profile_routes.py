from fastapi import APIRouter, HTTPException
import storage.json_storage as storage
from models.profile_models import Profile, ProfileUpdate

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
    "message": "Profile succesfuly created",
    "profile": profile.model_dump()
    }

@router.put("/profile")
def update_profile(profile_update: ProfileUpdate):

    current_profile = storage.load_profile()

    if current_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    update_data = profile_update.model_dump(exclude_unset=True)

    updated_profile = current_profile.model_copy(update=update_data)

    storage.save_profile(updated_profile)

    return {
        "message": "Profile successfully updated",
        "profile": updated_profile.model_dump()
    }