from argparse import Action
from crewai import Crew, Process
from agents import ArnetteBrainAgents
from tasks import ArnetteBrainTasks
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from colorama import Back


class ArnetteBrain:
    def __init__(self):

        print(Back.GREEN + "Arnette Brain is running" + Back.RESET)

        # Get environment variables
        load_dotenv()

        # Initialize local LLM
        self.llm = None

        # Set up agents and tasks
        self._agents = ArnetteBrainAgents()
        self._tasks = ArnetteBrainTasks()

        # AGENTS
        self._text_analyzer_agent = self._agents.text_analyzer_agent()

    # ------------------------------
    #  PUBLIC METHODS
    # ------------------------------
    def percieve_text(self, text):
        """
        Analyzes the text and returns the action and object of the action.

        Example output for "Please, make me some coffee.":
        [
            {
            "action": "action_word",
            "object": "object_word"
            }
        ]
        """
        print(Back.GREEN + "Arnette Brain is perceiving text" + Back.RESET)

        # Define tasks
        self._text_analyzer_task = self._tasks.text_analyzer_task(
            agent=self._text_analyzer_agent, text=text
        )

        crew = Crew(
            agents=[self._text_analyzer_agent],
            tasks=[self._text_analyzer_task],
            process=Process.sequential,
            manager_llm=self.llm,
            verbose=2,
        )

        # Start the crew's work
        return crew.kickoff()
