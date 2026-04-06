import os
from dotenv import load_dotenv
from pathlib import Path
import yaml
from crewai import Agent, Crew, Process, Task, LLM
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

load_dotenv()

llm = LLM(
    model="huggingface/meta-llama/Llama-3.1-8B-Instruct",
)

class ResumeWritingCrew():
    """Resume Writing Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def _load_agent_config(self) -> dict:
        path = Path(__file__).parent / "config" / "agents.yaml"
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def _load_task_config(self) -> dict:
        path = Path(__file__).parent / "config" / "tasks.yaml"
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def _build_agents(self) -> List[Agent]:
        agents_config = self._load_agent_config()
        return [
            Agent(
                role=agents_config['job']['role'],
                goal=agents_config['job']['goal'],
                backstory=agents_config['job']['backstory'],
                verbose=True,
                llm=llm
            ),
            Agent(
                role=agents_config['profile']['role'],
                goal=agents_config['profile']['goal'],
                backstory=agents_config['profile']['backstory'],
                verbose=True,
                llm=llm
            ),
            Agent(
                role=agents_config['resume']['role'],
                goal=agents_config['resume']['goal'],
                backstory=agents_config['resume']['backstory'],
                verbose=True,
                llm=llm
            ),
        ]

    def _build_tasks(self, agents: List[Agent]) -> List[Task]:
        tasks_config = self._load_task_config()
        job_task = Task(
            description=tasks_config['job_task']['description'],
            expected_output=tasks_config['job_task']['expected_output'],
            agent=agents[0]
        )
        profile_task = Task(
            description=tasks_config['profile_task']['description'],
            expected_output=tasks_config['profile_task']['expected_output'],
            agent=agents[1],
            context=[job_task]
        )
        resume_task = Task(
            description=tasks_config['resume_task']['description'],
            expected_output=tasks_config['resume_task']['expected_output'],
            agent=agents[2],
            context=[job_task, profile_task],
            output_file="resume.md"
        )
        return [job_task, profile_task, resume_task]

    def crew(self) -> Crew:
        """Creates the research crew"""
        agents = self._build_agents()
        tasks = self._build_tasks(agents)
        self.agents = agents
        self.tasks = tasks
        return Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
        )