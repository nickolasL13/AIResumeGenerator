import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="Resume History", layout="wide")

st.title("Resume History")


def load_resumes():
    try:
        resp = requests.get(f"{BACKEND_URL}/resumes")
        if resp.status_code == 200:
            return resp.json().get("resumes", [])
    except requests.ConnectionError:
        pass
    return []


resumes = load_resumes()

if not resumes:
    st.info("No generated resumes yet. Go to **Generate Resume** to create one.")
    if st.button("Go to Generate Resume"):
        st.switch_page("pages/generate_resume.py")
    st.stop()

st.caption(f"{len(resumes)} resume(s) generated")

for r in resumes:
    with st.expander(f"{r.get('job_description_preview', 'N/A')[:80]}…  —  {r['timestamp']}"):
        col_view, col_dl = st.columns([1, 1])
        with col_view:
            if st.button("View", key=f"view_{r['filename']}"):
                try:
                    resp = requests.get(f"{BACKEND_URL}/resume/{r['filename']}")
                    if resp.status_code == 200:
                        st.session_state.viewed_resume = resp.json().get("content", "")
                        st.session_state.viewed_filename = r["filename"]
                    else:
                        st.error("Failed to load resume")
                except requests.ConnectionError:
                    st.error("Cannot connect to backend")
        with col_dl:
            if st.button("Download", key=f"dl_{r['filename']}"):
                try:
                    resp = requests.get(f"{BACKEND_URL}/resume/{r['filename']}")
                    if resp.status_code == 200:
                        st.session_state.viewed_resume = resp.json().get("content", "")
                        st.session_state.viewed_filename = r["filename"]
                except requests.ConnectionError:
                    st.error("Cannot connect to backend")

if st.session_state.get("viewed_resume"):
    st.divider()
    st.subheader(st.session_state.get("viewed_filename", "Resume"))
    st.markdown(st.session_state.viewed_resume)

    if st.button("Download as Markdown"):
        st.download_button(
            label="Download .md",
            data=st.session_state.viewed_resume,
            file_name=st.session_state.get("viewed_filename", "resume.md"),
            mime="text/markdown"
        )
