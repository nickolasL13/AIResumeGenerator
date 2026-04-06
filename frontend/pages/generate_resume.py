import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="Generate Resume", layout="wide")

st.title("Generate Resume")

with st.sidebar:
    st.header("Steps")
    st.caption(f"Backend: {BACKEND_URL}")

# Check profile exists
def has_profile():
    try:
        resp = requests.get(f"{BACKEND_URL}/profile")
        return resp.status_code == 200 and resp.json().get("profile")
    except requests.ConnectionError:
        return False

profile_data = None

if not has_profile():
    st.warning("You need to create a profile first.")
    if st.button("Go to Create Profile"):
        st.switch_page("pages/create_profile.py")
    st.stop()
else:
    resp = requests.get(f"{BACKEND_URL}/profile")
    profile_data = resp.json()["profile"]
    st.info(f"Loaded profile for **{profile_data['name']}**")

# Job description
st.subheader("Job Description")
job_description = st.text_area(
    "Paste the job posting description here",
    height=250,
    placeholder="We are looking for a Junior Backend Developer..."
)

if st.button("Generate Resume", type="primary") and job_description:
    with st.spinner("Generating your resume with CrewAI... This may take a while."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/resume/generate",
                json={"job_description": job_description},
                timeout=300
            )
            if response.status_code == 200:
                result = response.json().get("resume", "")
                st.session_state.generated_resume = result
            else:
                st.error(f"Failed: {response.status_code} - {response.text}")
        except requests.ConnectionError:
            st.error("Cannot connect to backend at " + BACKEND_URL)
        except requests.Timeout:
            st.error("Request timed out. The crew may still be working.")

if st.session_state.get("generated_resume"):
    st.divider()
    st.subheader("Your Generated Resume")
    st.markdown(st.session_state.generated_resume)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Copy to Clipboard"):
            st.write("Resume copied to clipboard!")
            st.code(st.session_state.generated_resume)
