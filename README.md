# AI Resume Generator

## 📌 About the Project

AI Resume Generator is a web application designed to **automatically generate and optimize professional resumes using artificial intelligence**. The goal of the project is to help users maintain a structured record of their professional experiences and generate tailored resumes quickly when applying for job opportunities.

Instead of manually editing multiple versions of a resume, the user stores their professional information in the system (such as work experience, education, projects, and skills). When needed, the system can analyze a job description and generate a **customized resume aligned with the requirements of that specific position**.

This project is also developed as an academic project focused on exploring **multi-agent AI systems**, where different agents collaborate to analyze job descriptions, organize user data, and generate optimized resumes.

The system is designed with a **local-first approach**, meaning user data can be stored locally to reduce security and privacy concerns while maintaining full control over personal information.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Allow users to **store and manage their professional information** in a structured format.
* Automatically **generate resumes based on stored experiences**.
* Adapt resumes to **specific job descriptions**.
* Experiment with **AI agent architectures** for task automation.
* Provide a practical demonstration of **AI-assisted productivity tools**.

---

## ⚙️ Core Features

* User profile creation and editing
* Structured storage of professional data (skills, education, experience, projects)
* Automatic resume generation
* Resume customization based on job descriptions
* Compatibility scoring between resume and job description
* Local data storage for improved privacy
* Switch between languages (starts with portuguese and english)

---

## 🧠 AI Architecture

The system uses a **multi-agent architecture** where different agents perform specialized tasks, such as:

* **Job Analysis Agent** – Extracts relevant requirements and keywords from job descriptions.
* **Profile Organizer Agent** – Structures and selects relevant information from the user's profile.
* **Resume Generation Agent** – Generates a resume adapted to the target job.
* **Evaluation Agent** – Analyzes compatibility between the generated resume and the job requirements.

These agents collaborate to produce a more relevant and optimized resume.

---

## 🛠️ Technologies

The project is being developed using the following technologies:

### Backend

* Python
* FastAPI

### AI and Agent Frameworks

* CrewAI
* Large Language Models (LLMs)

### Data Processing

* Text processing and embeddings

### Data Storage

* Local JSON files or SQLite database

### Frontend

* StreamLit

---

## 🔒 Privacy and Data Handling

The system is designed with a **local-first philosophy**, meaning user data can be stored locally on the user's machine. This approach minimizes risks related to sensitive personal information and allows users to maintain full control over their professional data.

---

## 🚀 Future Improvements

Planned improvements for future versions include:

* Advanced job description analysis
* Improved resume optimization strategies
* Export to multiple formats (PDF, DOCX, etc.)
* Integration with job platforms
* Enhanced compatibility scoring
* Improved user interface

---

## 📚 Academic Context

This project is being developed as part of a **Computer Science undergraduate thesis**, focusing on the exploration of **AI-driven automation and multi-agent systems for professional document generation**.

---

## 👨‍💻 Author

Developed by **Nickolas Lima Ferreira**.
