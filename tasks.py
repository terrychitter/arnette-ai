from maps import actions, objects
from crewai import Task
from agents import ArnetteBrainAgents


# Responsible for defining the tasks that the Arnette Brain will perform
class ArnetteBrainTasks:

    # Responsible for analyzing text and returning the action word and object of the action
    def text_analyzer_task(self, agent, text):
        return Task(
            description="Analyze the text and return the action word, as well as the object of the action. The text is: {}".format(
                text
            ),
            agent=agent,
            async_execution=False,
            expected_output="""[
                {
                "action": "make",
                "object": "coffee"
                },
                ...
            ]
            """,
        )

    # Responsible for mapping the percived action and object to acceptable outputs
    def action_mapper_task(self, agent, context):
        # Get acceptable actions and objects
        acceptable_actions = actions.actions
        acceptable_objects = objects.objects

        return Task(
            description="Map the perceived action and object to acceptable outputs. The acceptable actions are {}. And the acceptable objects are {}. The action and object to map is {}".format(
                acceptable_actions, acceptable_objects, context
            ),
            agent=agent,
            async_execution=False,
            expected_output="""[
                {
                "action": "make",
                "object": "coffee"
                },
                ...
            ]
            """,
        )
