from models.job_models import JobDescription
from models.profile_models import Profile
from models.resume_models import Resume
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_resume_service(profile: Profile, job_description: JobDescription):
    """
    Receives user profile and job description then creates a CV based on both 
    """
    resume = Resume(
    summary="Desenvolvedor backend com experiência em APIs REST, bancos de dados relacionais e processamento de dados. Focado em escrever código limpo, escalável e de fácil manutenção.",
        profile={
            "name": "John Doe",
            "email": "john.doe@email.com",
            "skills": [
                {"category": "Backend", "name": "Python", "level": "Avançado"},
                {"category": "Backend", "name": "Node.js", "level": "Intermediário"},
                {"category": "Banco de Dados", "name": "PostgreSQL", "level": "Avançado"},
                {"category": "Ferramentas", "name": "Docker", "level": "Intermediário"}
            ],
            "education": [
                {
                    "degree": "Bacharelado em Ciência da Computação",
                    "institution": "University of California",
                    "finished": True,
                    "duration": {
                        "start": "2016-09-01",
                        "end": "2020-06-30"
                    }
                }
            ],
            "experience": [
                {
                    "role": "Backend Developer",
                    "company": "Tech Solutions Inc.",
                    "description": "Desenvolvimento de APIs REST em Python, integração com bancos de dados PostgreSQL e otimização de queries para alto desempenho.",
                    "duration": {
                        "start": "2021-01-01",
                        "end": "2023-12-31"
                    }
                },
                {
                    "role": "Junior Backend Developer",
                    "company": "Startup XYZ",
                    "description": "Atuação no desenvolvimento de serviços em Node.js, criação de endpoints e manutenção de sistemas existentes.",
                    "duration": {
                        "start": "2020-07-01",
                        "end": "2020-12-31"
                    }
                }
            ],
            "projects": [
                {
                    "name": "Task Manager API",
                    "description": "API REST para gerenciamento de tarefas com autenticação JWT e deploy em Docker.",
                    "link": "https://github.com/johndoe/task-manager"
                },
                {
                    "name": "Data Processing Pipeline",
                    "description": "Pipeline de processamento de dados utilizando Python e filas assíncronas.",
                    "link": None
                }
            ]
        }
    )

    prompt = f"""
        Crie um currículo profissional com beseado no seguinte json:

        {resume.model_dump_json()}

        O currículo deve ser bem escrito, organizado e profissional específico para a vaga abaixo:

        {job_description}

        Não use JSON. Apenas texto formatado no formato markdown.
        """
    
    API_URL = os.environ["API_URL"]
    headers = {
        "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    response = query({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "meta-llama/Llama-3.1-8B-Instruct:novita"
    })

    return response["choices"][0]["message"]