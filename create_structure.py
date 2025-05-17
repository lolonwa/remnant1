import os

# Function to create the directory structure and add files with inline documentation
def create_structure():
    # Define the folder structure
    folders = [
        "remnant/core",
        "remnant/interface",
        "remnant/services",
        "remnant/utils"
    ]

    # Define the files to be created in each folder
    files = {
        "remnant/core": [
            "__init__.py",
            "migration_advisor.py",
            "scam_detection.py",
            "scholarship_finder.py",
            "visa_info.py"
        ],
        "remnant/interface": [
            "__init__.py",
            "cli.py"
        ],
        "remnant/services": [
            "__init__.py",
            "llm_service.py"
        ],
        "remnant/utils": [
            "__init__.py",
            "user_context.py"
        ],
        "remnant": [
            "main.py",
            "requirements.txt",
            "README.md"
        ]
    }

    # Create directories
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files with initial content and detailed comments
    for folder, files_list in files.items():
        for file_name in files_list:
            file_path = os.path.join(folder, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    # Write common headers and detailed documentation
                    file.write(f"# {file_name} - Auto-generated module in {folder}\n\n")
                    file.write(f'"""\nModule: {file_name}\nLocation: {folder}\nPurpose: Describe the functionality here.\n"""\n\n')

                    if file_name == "migration_advisor.py":
                        file.write('''
class MigrationAdvisor:
    """
    Handles logic to advise users on migration paths based on their context.
    This includes study, work, asylum, and other possible routes.
    """

    def __init__(self, llm_service):
        """
        Initialize with a reference to an LLMService instance.
        """
        self.llm_service = llm_service

    def advise(self, user_context):
        """
        Use LLM to analyze user context and return migration advice.
        """
        prompt = f"What is the best migration option for: {user_context}?"
        return self.llm_service.query_llm(prompt)
''')

                    elif file_name == "scam_detection.py":
                        file.write('''
class ScamDetector:
    """
    Detects potential scam or fake job/visa offers using LLM analysis.
    """

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def analyze_offer(self, text):
        """
        Analyze a given job or visa offer for red flags.
        """
        prompt = f"Is this a scam? Analyze this offer: {text}"
        return self.llm_service.query_llm(prompt)
''')

                    elif file_name == "scholarship_finder.py":
                        file.write('''
class ScholarshipFinder:
    """
    Finds scholarship information using LLM search.
    """

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def find(self, country, level):
        """
        Query scholarships based on country and level of study.
        """
        prompt = f"Find scholarships in {country} for {level} level."
        return self.llm_service.query_llm(prompt)
''')

                    elif file_name == "visa_info.py":
                        file.write('''
class VisaInfoAdvisor:
    """
    Provides visa requirements and insights based on country and purpose.
    """

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def get_requirements(self, country, purpose):
        """
        Get visa requirements for a specific country and purpose.
        """
        prompt = f"What are the visa requirements for {country} for {purpose}?"
        return self.llm_service.query_llm(prompt)
''')

                    elif file_name == "llm_service.py":
                        file.write('''
class LLMService:
    """
    Mock or real LLM service handler. Replace `query_llm` with real integration.
    """

    def query_llm(self, prompt: str) -> str:
        """
        Sends prompt to LLM (mocked for now). Replace with actual API call.
        """
        return f"[Mock LLM response for prompt: {prompt}]"
''')

                    elif file_name == "cli.py":
                        file.write('''
from remnant.services.llm_service import LLMService
from remnant.core.migration_advisor import MigrationAdvisor
from remnant.utils.user_context import UserContext

def run_cli():
    """
    Entry point for CLI interaction. Asks user questions and advises on migration.
    """
    print("Welcome to Remnant Migration Advisor CLI")
    name = input("What is your name? ")
    goal = input("What is your migration goal? (study/work/asylum): ")
    country = input("Which country are you considering? ")
    age = input("What is your age? ")
    budget = input("What is your budget in USD? ")

    context = UserContext(name, goal, country, age, budget)
    advisor = MigrationAdvisor(LLMService())
    advice = advisor.advise(context)
    print(f"\\nAdvice for {name}: {advice}")
''')

                    elif file_name == "user_context.py":
                        file.write('''
class UserContext:
    """
    Stores user context needed to generate personalized migration advice.
    """

    def __init__(self, name, goal, country, age, budget):
        self.name = name
        self.goal = goal
        self.country = country
        self.age = age
        self.budget = budget

    def __str__(self):
        return f"{self.name}, age {self.age}, wants to {self.goal} in {self.country} with budget {self.budget}"
''')

                    elif file_name == "main.py":
                        file.write('''
from remnant.interface.cli import run_cli

if __name__ == "__main__":
    run_cli()
''')

                    elif file_name == "requirements.txt":
                        file.write("# Add external dependencies here, e.g., openai, langchain, etc.\n")

                    elif file_name == "README.md":
                        file.write('''
# Remnant - Migration Advisor App

## Purpose
Guide users in making informed migration decisions using LLMs.
Focus: student, work, asylum routes + scam detection + scholarships.

## Run Instructions (VS Code)
1. Open folder in VS Code
2. Create virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # or env\\Scripts\\activate on Windows''')
create_structure()