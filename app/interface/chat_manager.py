# app/interface/streamlit/chat_manager.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# app/interface/chat_manager.py

from app.services.llm_service import LLMService
from app.utils.user_context import UserContext
from app.utils.prompt_factory import PromptFactory
from app.core.migration_advisor import MigrationAdvisor
from app.core.scam_detection import ScamDetector
from app.core.scholarship_finder import ScholarshipFinder
from app.core.visa_info import VisaInfoAdvisor

class ChatManager:
    def __init__(self):
        self.state = {
            "mode": None,
            "name": None,
            "goal": None,
            "country": None,
            "age": None,
            "budget": None,
            "step": 0,
            "scam_text": None
        }
        self.llm = LLMService()

    def handle_user_input(self, user_input):
        step = self.state["step"]

        if step == 0:
            # 🔁 Switch tools mid-chat (optional shortcut)
            tool_switch_phrases = {
                "migration": "1",
                "scam": "2",
                "scholarship": "3",
                "visa": "4"
            }
            for key, value in tool_switch_phrases.items():
                if key in user_input.lower():
                    self.reset()
                    return self.handle_user_input(value)

            # Show menu
            menu = (
                "Hi, how can I help you?\n"
                "Please choose an option:\n"
                "1. Migration Advice\n"
                "2. Scam Detector\n"
                "3. Scholarship Finder\n"
                "4. Visa Info"
            )
            self.state["step"] += 1  # ✅ Make sure we go to step 1
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
            if self.state["mode"] == "scam_detector":
                return "🔁 Switching to Scam Detector! Please paste the text you want to analyze for scams."
            return "Let's get started. What is your name?"

        # Step 2 — name or scam text
        elif step == 2 and self.state["mode"] != "scam_detector":
            self.state["name"] = user_input
            self.state["step"] += 1
            return f"Hi {user_input}! What is your migration goal? (study / work / asylum)"

        elif step == 2 and self.state["mode"] == "scam_detector":
            self.state["scam_text"] = user_input
            return self.analyze_scam(user_input)

        # Step 3 — goal
        elif step == 3:
            self.state["goal"] = user_input.lower()
            self.state["step"] += 1
            return f"Great. Which country are you considering for {self.state['goal']}?"

        # Step 4 — country
        elif step == 4:
            self.state["country"] = user_input
            self.state["step"] += 1
            return "What is your age?"

        # Step 5 — age
        elif step == 5:
            self.state["age"] = user_input
            self.state["step"] += 1
            return "What is your budget in USD?"

        # Step 6 — budget and final processing
        elif step == 6:
            self.state["budget"] = user_input
            self.state["step"] += 1
            return self._handle_selected_mode()

        else:
            return "You can ask a follow-up question or type 'restart' to begin again."


    def analyze_scam(self, text):
        red_flags = []
        advice = ""

        checks = {
            "Promises a huge amount of money for free": ["you've been selected", "congratulations", "you won", "million dollars"],
            "Asks for money upfront": ["processing fee", "send money", "wire transfer", "bank account"],
            "Asks for personal information": ["full name", "home address", "phone number", "ID number"],
            "Tries to create urgency": ["expires in", "act now", "urgent", "24 hours"],
            "Uses suspicious email or contact info": ["@", ".com", "reply now"],
            "Vague or no mention of real organization": ["lottery", "prize", "winner", "opportunity"]
        }

        total_checks = 0
        failed_checks = 0

        for reason, keywords in checks.items():
            total_checks += 1
            if any(word in text.lower() for word in keywords):
                red_flags.append(reason)
                failed_checks += 1

        percentage = int((failed_checks / total_checks) * 100)
        is_scam = percentage >= 50

        if is_scam:
            advice = (
                "⚠️ This is likely a scam! Never share personal info or send money to unknown people. "
                "Real organizations don’t ask for fees to claim prizes. 🚫"
            )
        else:
            advice = (
                "✅ This doesn’t seem like a scam, but always double-check. Stay safe online! 🌐"
            )

        return (
            f"🔍 Scam Detection Report:\n\n"
            f"🎯 Scam Likelihood: {percentage}%\n"
            f"✅ Is this a scam? {'YES' if is_scam else 'NO'}\n\n"
            f"🚨 Red Flags:\n" + '\n'.join(f"- {flag}" for flag in red_flags) + "\n\n"
            f"💡 Advice:\n{advice}"
        )

    def _handle_selected_mode(self):
        context = UserContext(
            name=self.state["name"],
            goal=self.state["goal"],
            country=self.state["country"],
            age=self.state["age"],
            budget=self.state["budget"],
        )

        if self.state["mode"] == "migration_advice":
            advisor = MigrationAdvisor(self.llm)
            response = advisor.advise(context)
            return f"Here is your personalized migration advice:\n\n{response}"
        elif self.state["mode"] == "scam_detector":
            return self.analyze_scam(self.state["scam_text"])
        elif self.state["mode"] == "scholarship_finder":
            finder = ScholarshipFinder(self.llm)
            result = finder.find_scholarships(str(context.__dict__))
            return f"Scholarship search result (based on your info):\n\n{result}"
        elif self.state["mode"] == "visa_info":
            visa = VisaInfoAdvisor(self.llm)
            result = visa.get_info(str(context.__dict__))
            return f"Visa info result (based on your info):\n\n{result}"
        else:
            return "Unknown mode."

    def reset(self):
        self.state = {
            "mode": None,
            "name": None,
            "goal": None,
            "country": None,
            "age": None,
            "budget": None,
            "step": 0,
            "scam_text": None
        }
