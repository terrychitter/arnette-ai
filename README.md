# Arnette AI
Arnette AI is a conversational/assist AI that makes use of Large Language Models (LLMs) to respond to users and their requests or commands.
**Note:** This project is still a work-in-progress and will not perform fully to the description.

## Installation and Configuration

### Poetry
1. Download or clone the repository into the directory of your choice.
2. If you do not already have poetry installed on your machine run `pip install poetry`
3. Install python dependencies using `poetry install --no-root`
4. Create a virtual python environment with poetry using `poetry shell`

### Ollama and Local LLMs
This project makes use of local LLMs (**Specifically Llama2**) to power Arnette AI. See the steps below to download and install your own LLM:
1. Download Ollama [here](https://ollama.com) if you have not already done so.
2. Once Ollama has been successfully installed. Open the terminal and run `ollama pull llama2`.
3. Once Llama2 has been successfully downloaded, navigate to the repository's root and run `ollama create crewai-llama2 -f ./setup/llama2_model_file`

### Environment Variables
Ensure that you have provided the correct environment variables and that you have renamed `.env.example` to `.env`. If you are also using the llama2 local LLM then your `.env` should be similar, if not, identical to the below snippet:
```
OPENAI_API_BASE='http://localhost:11434/v1'
OPENAI_MODEL_NAME=crewai-llama2
OPENAI_API_KEY=NA
```
If you are using a different LLM then it is important to note that you should also update the `main.py` file.
```
# Initialize the Local LLM
llm = ChatOpenAI(model="crewai-llama2", base_url="http://localhost:11434/v1")
```

## Run the project
To run the project simply run the main python file using the terminal: `python main.py`

## Contributing
Contributions from the community are most welcomed! Whether it's reporting a bug, submitting a feature request, or improving the documentation, your help is appreciated. To contribute to this project, please follow these guidelines:

### Issues and Bugs
If you encounter any issues or find a bug, please check the existing issues to see if it has already been reported. If not, please open a new issue, including the following details:

- A clear and descriptive title.
- A detailed description of the issue, including steps to reproduce.
- Screenshots or code snippets, if applicable.
- Information about your environment (operating system, browser, etc.).

### Feature Requests
You are welcome to suggest new features or improvements. Before submitting a feature request, please:
- Check the existing feature requests to avoid duplicates.
- Provide a clear and detailed description of the proposed feature.
- Discuss the feature with the community to gather feedback.

### Pull Requests
Pull requests for bug fixes, new features, and improvements are welcomed as well. To submit a pull request, follow these steps:

- Fork the repository and create a new branch for your contribution.
- Write clear and comprehensive commit messages.
- Test your changes thoroughly.
- Submit a pull request, referencing the relevant issue (if applicable).
- Be prepared to address feedback and iterate on your changes.

By contributing to this project, you agree that your contributions will be licensed under the project's license.
Thank you for contributing to the project! 🚀
