from fastapi import FastAPI
from api.profile_routes import router as profile_router

app = FastAPI(
    title='AI Resume Generator',
    description='AI system for generating job-specific resumes',
    version='0.1'
)

app.include_router(profile_router)

@app.get("/")
def root():
    return {"message": "API running"}