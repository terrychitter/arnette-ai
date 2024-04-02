from brain import ArnetteBrain
from maps import actions, objects
from langchain_openai import ChatOpenAI

# Initialize the Arnette Brain
arnette_brain = ArnetteBrain()

# Set the LLM
arnette_brain.llm = ChatOpenAI(
    model="crewai-mistral", base_url="http://localhost:11434/v1"
)

if __name__ == "__main__":
    while True:
        # Get the user's input
        user_input = input("Enter a sentence/command: ")

        # Percieve the text and present the results
        analysis = arnette_brain.percieve_text(user_input)

        # Print the results
        print("Action:")
        print(analysis)
