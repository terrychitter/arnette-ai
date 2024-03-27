from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import ArnetteBrainAgents
from tasks import ArnetteBrainTasks

# Get environment variables
from dotenv import load_dotenv

load_dotenv()

# Initialize the Local LLM
llm = ChatOpenAI(model="crewai-llama2", base_url="http://localhost:11434/v1")

# Set up agents and tasks
agents = ArnetteBrainAgents()
tasks = ArnetteBrainTasks()

# Instantiate agents
text_analyzer_agent = agents.text_analyzer_agent()
action_mapper_agent = agents.action_mapper_agent()

# Instantiate tasks
text_analyzer_task = tasks.text_analyzer_task(
    text_analyzer_agent, "Please, make me a cup of coffee."
)
action_mapper_task = tasks.action_mapper_task(action_mapper_agent, text_analyzer_task)

# Form the crew
crew = Crew(
    agents=[text_analyzer_agent, action_mapper_agent],
    tasks=[text_analyzer_task, action_mapper_task],
    process=Process.sequential,
    manager_llm=ChatOpenAI,
    verbose=2,
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)
