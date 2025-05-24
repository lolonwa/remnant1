# app/interface/streamlit/chat_manager.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from app.services.llm_service import LLMService
from app.utils.user_context import UserContext
from app.utils.prompt_factory import PromptFactory
from app.core.migration_advisor import MigrationAdvisor
from app.core.scam_detection import ScamDetector
from app.core.scholarship_finder import ScholarshipFinder
from app.core.visa_info import VisaInfo

class ChatManager:
    def __init__(self):
        self.state = {
            "mode": None,  # new: stores selected mode
            "name": None,
            "goal": None,
            "country": None,
            "age": None,
            "budget": None,
            "step": 0,
        }
        self.llm = LLMService()

    def handle_user_input(self, user_input):
        step = self.state["step"]

        if step == 0:
            # Show menu
            menu = (
                "Hi, how can I help you?\n"
                "Please choose an option:\n"
                "1. Migration Advice\n"
                "2. Scam Detector\n"
                "3. Scholarship Finder\n"
                "4. Visa Info"
            )
            self.state["step"] += 1
            return menu

        elif step == 1:
            # Handle menu selection
            options = {
                "1": "migration_advice",
                "2": "scam_detector",
                "3": "scholarship_finder",
                "4": "visa_info"
            }
            choice = user_input.strip()
            if choice not in options:
                return "Please enter a valid option number (1-4)."
            self.state["mode"] = options[choice]
            self.state["step"] += 1

            if self.state["mode"] == "migration_advice":
                return "Let's get started with migration advice. What is your name?"
            elif self.state["mode"] == "scam_detector":
                return "Paste the offer or message you want to check for scams."
            elif self.state["mode"] == "scholarship_finder":
                return "What country or field are you interested in for scholarships?"
            elif self.state["mode"] == "visa_info":
                return "Which country's visa information do you need?"

        # Migration Advice flow
        elif self.state["mode"] == "migration_advice":
            if step == 2:
                self.state["name"] = user_input
                self.state["step"] += 1
                return f"Hi {user_input}! What is your migration goal? (study / work / asylum)"
            elif step == 3:
                self.state["goal"] = user_input.lower()
                self.state["step"] += 1
                return f"Great. Which country are you considering for {self.state['goal']}?"
            elif step == 4:
                self.state["country"] = user_input
                self.state["step"] += 1
                return "What is your age?"
            elif step == 5:
                self.state["age"] = user_input
                self.state["step"] += 1
                return "What is your budget in USD?"
            elif step == 6:
                self.state["budget"] = user_input
                self.state["step"] += 1
                return self._generate_advice()
            else:
                return "You can ask a follow-up question or type 'restart' to begin again."

        # Add similar flows for scam_detector, scholarship_finder, visa_info as needed
        elif self.state["mode"] == "scam_detector":
            # Only ask once, then analyze
            detector = ScamDetector(self.llm)
            result = detector.analyze_offer(user_input)
            return f"Scam detection result:\n\n{result}"

        elif self.state["mode"] == "scholarship_finder":
            # Only ask once, then search
            finder = ScholarshipFinder(self.llm)
            result = finder.find_scholarships(user_input)
            return f"Scholarship search result:\n\n{result}"

        elif self.state["mode"] == "visa_info":
            # Only ask once, then provide info
            visa = VisaInfo(self.llm)
            result = visa.get_info(user_input)
            return f"Visa info result:\n\n{result}"

        else:
            return "You can ask a follow-up question or type 'restart' to begin again."

    def _generate_advice(self):
        context = UserContext(
            name=self.state["name"],
            goal=self.state["goal"],
            country=self.state["country"],
            age=self.state["age"],
            budget=self.state["budget"],
        )
        advisor = MigrationAdvisor(self.llm)
        response = advisor.advise(context)
        return f"Here is your personalized advice:\n\n{response}"
