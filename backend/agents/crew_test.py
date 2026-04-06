from crew import ResumeWritingCrew 

job_description = """
We are looking for a Junior Backend Developer to join our team.

The candidate will be responsible for developing and maintaining REST APIs, working with relational databases, and supporting backend services. You will collaborate with the team to build scalable and efficient systems.

Requirements:
- Basic experience with Python or Node.js
- Knowledge of REST APIs
- Familiarity with PostgreSQL or other relational databases
- Understanding of Git

Nice to have:
- Experience with Docker
- Basic knowledge of cloud services
"""

profile = {
  "name": "Alice Johnson",
  "email": "alice.johnson@email.com",
  "skills": [
    { "category": "Backend", "name": "Python", "level": "Intermediário" },
    { "category": "Backend", "name": "Node.js", "level": "Básico" },
    { "category": "Banco de Dados", "name": "PostgreSQL", "level": "Intermediário" },
    { "category": "Ferramentas", "name": "Git", "level": "Intermediário" },
    { "category": "Ferramentas", "name": "Docker", "level": "Básico" }
  ],
  "education": [
    {
      "degree": "Bacharelado em Ciência da Computação",
      "institution": "Federal University of Ceará",
      "finished": True,
      "duration": {
        "start": "2019-01-01",
        "end": "2023-12-31"
      }
    }
  ],
  "experience": [
    {
      "role": "Intern Backend Developer",
      "company": "TechStart",
      "description": "Auxiliou no desenvolvimento de APIs REST em Python e na integração com banco de dados PostgreSQL.",
      "duration": {
        "start": "2022-01-01",
        "end": "2022-12-31"
      }
    },
    {
      "role": "Junior Backend Developer",
      "company": "DevSolutions",
      "description": "Desenvolvimento e manutenção de APIs em Node.js, implementação de endpoints e suporte a serviços backend.",
      "duration": {
        "start": "2023-01-01",
        "end": "2024-06-01"
      }
    }
  ],
  "projects": [
    {
      "name": "Task API",
      "description": "API REST para gerenciamento de tarefas utilizando Python e PostgreSQL.",
      "link": "https://github.com/alice/task-api"
    },
    {
      "name": "Simple Auth System",
      "description": "Sistema de autenticação com Node.js usando JWT.",
      "link": None
    }
  ]
}

def run():
    """
    Run the research crew.
    """
    inputs = {
        'profile': profile,
        'job_description': job_description
    }

    # Create and run the crew
    result = ResumeWritingCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")


run()