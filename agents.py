from crewai import Agent


class ArnetteBrainAgents:

    # Responsible for analyzing text and returning the action word and object of the action
    def text_analyzer_agent(self):
        return Agent(
            role="Text Analyzer",
            goal="Analyze the text and return the action word, as well as the object of the action.",
            backstory="""
            You are a section of Arnette's digital brain responsible for making sense of sentences and commands.
            """,
            verbose=True,
            allow_delegation=False,
        )

    # Responsible for mapping the percieved action and object to acceptable outputs
    def action_mapper_agent(self):
        return Agent(
            role="Action Mapper",
            goal="Map the perceived action and object to acceptable outputs.",
            backstory="""
            You are a section of Arnette's digital brain responsible for mapping the perceived action and object to acceptable outputs.
            """,
            verbose=True,
            allow_delegation=False,
        )
