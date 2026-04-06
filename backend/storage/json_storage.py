import json
from pathlib import Path
from datetime import datetime
from models.profile_models import Profile

DATA_PATH = Path("data")
PROFILE_FILE = DATA_PATH / "user_profile.json"
RESUMES_DIR = DATA_PATH / "resumes"

def _ensure_dir():
    DATA_PATH.mkdir(exist_ok=True)

def _ensure_resumes_dir():
    RESUMES_DIR.mkdir(exist_ok=True)

def save_profile(profile: Profile):
    _ensure_dir()

    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile.model_dump(mode="json"), f, indent=2)


def load_profile() -> Profile | None:
    if not PROFILE_FILE.exists():
        return None

    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return Profile(**data)


def save_resume(job_description: str, resume_content: str) -> dict:
    _ensure_resumes_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"resume_{timestamp}.md"
    filepath = RESUMES_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(resume_content)

    metadata = {
        "filename": filename,
        "timestamp": timestamp,
        "job_description_preview": job_description[:150]
    }
    meta_path = RESUMES_DIR / f"resume_{timestamp}_meta.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    return metadata


def list_resumes() -> list[dict]:
    _ensure_resumes_dir()
    resumes = []
    for meta_file in sorted(RESUMES_DIR.glob("resume_*_meta.json"), reverse=True):
        with open(meta_file, "r", encoding="utf-8") as f:
            resumes.append(json.load(f))
    return resumes


def load_resume(filename: str) -> str | None:
    filepath = RESUMES_DIR / filename
    if not filepath.exists():
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()