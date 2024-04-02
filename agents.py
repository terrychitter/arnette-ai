from crewai import Agent


class ArnetteBrainAgents:

    # Responsible for analyzing text and returning the action word and object of the action
    def text_analyzer_agent(self):
        return Agent(
            role="Text Analyzer",
            goal="Accurately identify the action (command) and the object (target) of a given sentence.",
            backstory="""
            You are currently a section in a digital brain responsible for language comprehension.
            You are equipped with advanced natural language processing capabilities and have been
            trained extensively on understanding various forms of human communication.
            """,
            max_iter=1,
            verbose=True,
            allow_delegation=False,
            memory=True,
        )
