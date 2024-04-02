from maps import actions, objects
from crewai import Task
from agents import ArnetteBrainAgents
from colorama import Fore, Back


# Responsible for defining the tasks that the Arnette Brain will perform
class ArnetteBrainTasks:

    # Responsible for analyzing text and returning the action word and object of the action
    def text_analyzer_task(self, agent, text):
        print(Back.GREEN + "Text Analyzer Task is running" + Back.RESET)
        return Task(
            description=f"Determine the action and command word from following text: {text}",
            agent=agent,
            async_execution=False,
            expected_output="""
                {
                "action": "action_word",
                "object": "object_word"
                }
            """,
        )
