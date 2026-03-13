import json
from pathlib import Path
from models.profile_models import Profile

DATA_PATH = Path("data")
PROFILE_FILE = DATA_PATH / "user_profile.json"

def save_profile(profile: Profile):
    DATA_PATH.mkdir(exist_ok=True)

    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile.model_dump(mode="json"), f, indent=2)


def load_profile() -> Profile | None:
    if not PROFILE_FILE.exists():
        return None

    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return Profile(**data)