import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def render_create_profile():
    if not st.session_state.get("current_profile"):
        st.session_state.current_profile = {
            "name": "",
            "email": "",
            "skills": [],
            "education": [],
            "experience": [],
            "projects": [],
        }

    profile = st.session_state.current_profile

    st.header("Create your profile")
    st.caption("This data will be tailored to job descriptions")

    # Basic info
    st.subheader("Basic Info")
    col1, col2 = st.columns(2)
    with col1:
        profile["name"] = st.text_input(
            "Name", value=profile["name"],
            placeholder="Alan Doe"
        )
    with col2:
        profile["email"] = st.text_input(
            "Email", value=profile["email"],
            placeholder="alan.doe@email.com"
        )

    # Skills
    st.subheader("Skills")
    _render_skills(profile)

    # Education
    st.subheader("Education")
    _render_education(profile)

    # Experience
    st.subheader("Experience")
    _render_experience(profile)

    # Projects
    st.subheader("Projects")
    _render_projects(profile)

    # Actions
    st.divider()
    col_back, col_save = st.columns([1, 2])
    with col_back:
        if st.button("Back"):
            st.session_state.page = "home"
            st.rerun()
    with col_save:
        if st.button("Save Profile", type="primary"):
            _save_profile(profile)


def _render_skills(profile):
    for i, skill in enumerate(profile["skills"]):
        c1, c2, c3, c4 = st.columns([2, 2, 2, 0.5])
        with c1:
            profile["skills"][i]["category"] = st.text_input(
                "Category", value=skill["category"],
                key=f"skill_cat_{i}"
            )
        with c2:
            profile["skills"][i]["name"] = st.text_input(
                "Name", value=skill["name"],
                key=f"skill_name_{i}"
            )
        with c3:
            profile["skills"][i]["level"] = st.selectbox(
                "Level",
                options=["Not necessary", "Beginner", "Intermediate", "Advanced"],
                index=["Not necessary", "Beginner", "Intermediate", "Advanced"].index(
                    skill.get("level") or "Not necessary"
                ),
                key=f"skill_lvl_{i}"
            )
        with c4:
            if st.button("X", key=f"del_skill_{i}"):
                profile["skills"].pop(i)
                st.rerun()

    sc1, sc2 = st.columns([2, 1])
    with sc1:
        if st.button("Add Skill"):
            profile["skills"].append({
                "category": "", "name": "", "level": "Intermediate"
            })
            st.rerun()
    with sc2:
        st.caption(f"{len(profile['skills'])} skill(s)")


def _render_education(profile):
    for i, edu in enumerate(profile["education"]):
        dur = edu.get("duration", {})
        with st.expander(
            f"{edu.get('degree') or 'Education'} - {edu.get('institution') or 'Institution'}"
            if edu.get("degree") or edu.get("institution")
            else f"Education #{i+1}",
            expanded=True
        ):
            c1, c2 = st.columns(2)
            with c1:
                profile["education"][i]["degree"] = st.text_input(
                    "Degree", value=edu.get("degree", ""),
                    key=f"edu_degree_{i}"
                )
            with c2:
                profile["education"][i]["institution"] = st.text_input(
                    "Institution", value=edu.get("institution", ""),
                    key=f"edu_inst_{i}"
                )
            c3, c4 = st.columns(2)
            with c3:
                start_date = None
                if dur.get("start"):
                    try:
                        start_date = __import__("datetime").date.fromisoformat(dur["start"])
                    except (ValueError, TypeError):
                        pass
                profile["education"][i]["duration"] = profile["education"][i].get("duration", {})
                start_val = st.date_input("Start", value=start_date, key=f"edu_start_{i}")
                profile["education"][i]["duration"]["start"] = start_val.isoformat()
            with c4:
                end_date = None
                if dur.get("end"):
                    try:
                        end_date = __import__("datetime").date.fromisoformat(dur["end"])
                    except (ValueError, TypeError):
                        pass
                end_val = st.date_input("End", value=end_date, key=f"edu_end_{i}")
                profile["education"][i]["duration"]["end"] = end_val.isoformat()
                if profile["education"][i].get("finished", False):
                    profile["education"][i]["duration"]["end"] = end_val.isoformat()
            c5, c6 = st.columns(2)
            with c5:
                profile["education"][i]["finished"] = st.checkbox(
                    "Finished?", value=edu.get("finished", False),
                    key=f"edu_fin_{i}"
                )
            with c6:
                if st.button("Remove", key=f"del_edu_{i}"):
                    profile["education"].pop(i)
                    st.rerun()

    if st.button("Add Education"):
        today = __import__("datetime").date.today().isoformat()
        profile["education"].append({
            "degree": "", "institution": "", "finished": False,
            "duration": {"start": today, "end": today}
        })
        st.rerun()


def _render_experience(profile):
    for i, exp in enumerate(profile["experience"]):
        title = exp.get("role") or f"Experience #{i+1}"
        company = exp.get("company") or ""
        dur = exp.get("duration", {})
        with st.expander(f"{title} at {company}" if company else title, expanded=True):
            c1, c2 = st.columns(2)
            with c1:
                profile["experience"][i]["role"] = st.text_input(
                    "Role", value=exp.get("role", ""),
                    key=f"exp_role_{i}"
                )
            with c2:
                profile["experience"][i]["company"] = st.text_input(
                    "Company", value=exp.get("company", ""),
                    key=f"exp_comp_{i}"
                )
            c3, c4 = st.columns(2)
            with c3:
                start_date = None
                if dur.get("start"):
                    try:
                        start_date = __import__("datetime").date.fromisoformat(dur["start"])
                    except (ValueError, TypeError):
                        pass
                profile["experience"][i]["duration"] = profile["experience"][i].get("duration", {})
                start_val = st.date_input("Start", value=start_date, key=f"exp_start_{i}")
                profile["experience"][i]["duration"]["start"] = start_val.isoformat()
            with c4:
                end_date = None
                if dur.get("end"):
                    try:
                        end_date = __import__("datetime").date.fromisoformat(dur["end"])
                    except (ValueError, TypeError):
                        pass
                end_val = st.date_input("End (leave in future if current role)", value=end_date, key=f"exp_end_{i}")
                profile["experience"][i]["duration"]["end"] = end_val.isoformat()
            profile["experience"][i]["description"] = st.text_area(
                "Description", value=exp.get("description", ""),
                key=f"exp_desc_{i}"
            )
            if st.button("Remove", key=f"del_exp_{i}"):
                profile["experience"].pop(i)
                st.rerun()

    if st.button("Add Experience"):
        today = __import__("datetime").date.today().isoformat()
        profile["experience"].append({
            "role": "", "company": "", "description": "",
            "duration": {"start": today, "end": today}
        })
        st.rerun()


def _render_projects(profile):
    for i, proj in enumerate(profile["projects"]):
        name = proj.get("name") or f"Project #{i+1}"
        with st.expander(name):
            profile["projects"][i]["name"] = st.text_input(
                "Name", value=proj.get("name", ""),
                key=f"proj_name_{i}"
            )
            profile["projects"][i]["description"] = st.text_area(
                "Description", value=proj.get("description", ""),
                key=f"proj_desc_{i}"
            )
            profile["projects"][i]["link"] = st.text_input(
                "Link (optional)", value=proj.get("link") or "",
                key=f"proj_link_{i}"
            )
            if st.button("Remove", key=f"del_proj_{i}"):
                profile["projects"].pop(i)
                st.rerun()

    if st.button("Add Project"):
        profile["projects"].append({
            "name": "", "description": "", "link": None
        })
        st.rerun()


def _save_profile(profile):
    if not profile["name"].strip() or not profile["email"].strip():
        st.error("Name and Email are required.")
        return

    payload = {
        "name": profile["name"].strip(),
        "email": profile["email"].strip(),
        "skills": [
            s for s in profile["skills"]
            if s.get("name", "").strip()
        ],
        "education": [
            e for e in profile["education"]
            if e.get("degree", "").strip()
        ],
        "experience": [
            e for e in profile["experience"]
            if e.get("role", "").strip()
        ],
        "projects": [
            p for p in profile["projects"]
            if p.get("name", "").strip()
        ],
    }

    # Fill in empty lists for missing sections
    if not payload["skills"]:
        profile["skills"] = []
    if not payload["education"]:
        profile["education"] = []
    if not payload["experience"]:
        profile["experience"] = []
    if not payload["projects"]:
        profile["projects"] = []

    try:
        response = requests.post(f"{BACKEND_URL}/profile", json=payload)
        if response.status_code in (200, 201):
            st.success("Profile saved successfully!")
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error(f"Failed to save: {response.text}")
    except requests.ConnectionError:
        st.error(
            "Cannot connect to backend. "
            "Make sure the API is running on " + BACKEND_URL
        )


render_create_profile()
