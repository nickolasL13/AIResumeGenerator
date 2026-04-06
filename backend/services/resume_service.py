from models.job_models import JobDescription
from models.profile_models import Profile
import json
import sys
from pathlib import Path

# Ensure backend root is importable when called from service
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

def generate_resume_service(profile: Profile, job_description: JobDescription) -> str:
    """
    Receives user profile and job description then creates a CV based on both
    using the CrewAI Crew.
    """
    # Delay import so crewai is only loaded when actually generating
    from agents.crew import ResumeWritingCrew

    # Format profile as dict readable by crew task placeholders
    profile_data = profile.model_dump(mode="json")

    inputs = {
        'profile': json.dumps(profile_data, indent=2),
        'job description': job_description.job_description,
    }

    result = ResumeWritingCrew().crew().kickoff(inputs=inputs)
    return result.raw