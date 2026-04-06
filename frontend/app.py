import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(
    page_title="AI Resume Generator",
    page_icon="✨",
    layout="wide"
)

st.title("AI Resume Generator")
st.caption("Create a personalized resume tailored to any job description")

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Create Profile", use_container_width=True):
        st.switch_page("pages/create_profile.py")
with col2:
    if st.button("Generate Resume", use_container_width=True):
        st.switch_page("pages/generate_resume.py")
with col3:
    if st.button("Resume History", use_container_width=True):
        st.switch_page("pages/resume_history.py")

st.divider()
st.markdown("""
### How it works
1. **Create your profile** — Add your name, skills, education, experience, and projects
2. **Generate your resume** — Paste a job description and get a tailored, ATS-friendly resume
""")

st.caption(f"Backend: {BACKEND_URL}")
