# app/interface/streamlit/chat_manager.py

import sys
import os
from app.core.trusted_sources import TrustedSourceLoader
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# app/interface/streamlit/chat_manager.py

# chat_manager.py - Handles smart conversation flow with minimal LLM cost

from app.services.llm_service import LLMService
from app.core.migration_advisor import MigrationAdvisor
from app.utils.user_context import UserContext
from app.core.scam_detection import ScamDetector
from app.core.scholarship_finder import ScholarshipFinder

class ChatManager:
    def __init__(self):
        self.context = {}
        self.llm = LLMService()

    def update_context(self, key, value):
        """Stores user input like age, goal, country, budget, etc."""
        self.context[key] = value

    def is_ready_for_advice(self):
        """Check if enough info has been collected to generate advice"""
        required_fields = ['goal', 'age', 'budget']
        return all(field in self.context for field in required_fields)

    def ask_follow_up(self):
        """If user doesn't know country, guide them based on goal"""
        goal = self.context.get('goal')
        if goal == "study":
            return (
                "You're interested in studying abroad. Do you want countries that allow you to bring family too?\n"
                "Or should I list countries with the easiest student visa policies?"
            )
        elif goal == "work":
            return (
                "You're looking to work abroad. Do you have a skill or trade? Some countries have skill shortages.\n"
                "Would you like me to list countries open to foreign workers with family?"
            )
        elif goal == "asylum":
            return "Asylum can be complex. Are you fleeing conflict or persecution? I can list possible destinations and support options."

        return "Can you clarify your goal?"

    def get_advice(self):
        """Send minimal but structured info to LLM"""
        structured_prompt = {
            "age": self.context.get("age"),
            "budget_usd": self.context.get("budget"),
            "goal": self.context.get("goal"),
            "family": self.context.get("has_family", False),
            "skill": self.context.get("skill"),
            "country_preference": self.context.get("country"),
        }

        return self.llm.ask("Suggest best visa or migration options", structured_prompt)
    def suggest_countries_for_goal(self):
        goal = self.context.get("goal")
        age = self.context.get("age")
        budget = self.context.get("budget")

        if not goal:
            return "Please tell me your goal first (e.g., study, work, asylum)."

        prompt = (
            f"A user wants to migrate abroad. Their goal is '{goal}'."
            f"{f' They are {age} years old.' if age else ''}"
            f"{f' Their budget is ${budget}.' if budget else ''} "
            "Which countries are best for this purpose, especially those with easier visa routes, lower rejection rates, or programs that include family?"
            " List 3–5 countries with a short explanation each."
        )

        return self.llm.query_llm(prompt)   
    def explore_country_options(self, country):
        goal = self.context.get("goal", "migration")  # default fallback
        prompt = (
            f"A user wants to migrate to {country} with the goal of {goal}. "
            f"What are the main visa pathways available? Please list them with short descriptions and typical requirements. "
            "Highlight any options that support bringing family or have low barriers."
        )
        return self.llm.query_llm(prompt)
    def handle_user_input(self, user_input):
        lowered = user_input.lower()

        # Step 1: Ask for mode if not set
        if "mode" not in self.context:
            options = ["migration", "scholarship", "scam", "visa"]
            # Detect mode from user input
            for opt in options:
                if opt in lowered:
                    self.context["mode"] = opt
                    break
            if "mode" not in self.context:
                return (
                    "How can I help you today? Please choose one:\n"
                    "- Migration advice\n"
                    "- Scholarship info\n"
                    "- Scam detection\n"
                    "- Visa info"
                )
            # After mode is set, prompt for next info
            if self.context["mode"] == "migration":
                return (
    "What is your main migration goal?\n"
    "1. Study\n2. Work\n3. Asylum\n\n"
    "You can type the number or the word."
)
            elif self.context["mode"] == "scholarship":
                return "Which country are you interested in for scholarships?"
            elif self.context["mode"] == "scam":
                return "Paste the message or offer you'd like me to check for scams."
            elif self.context["mode"] == "visa":
                return "Which country's visa information do you need?"

        # Step 2: Route to the correct logic
        mode = self.context["mode"]

        if mode == "scholarship":
            if not self.context.get("country"):
                self.context["country"] = user_input
                return "What level of study? (undergraduate, masters, phd)"
            if not self.context.get("level"):
                self.context["level"] = user_input
                finder = ScholarshipFinder(self.llm)
                result = finder.find(self.context["country"], self.context["level"])
                self.context.clear()
                return result

        elif mode == "scam":
            detector = ScamDetector(self.llm)
            result = detector.analyze_offer(user_input)
            self.context.clear()
            return result

        elif mode == "visa":
            # Implement visa info logic here
            return "Visa info feature coming soon!"

        # Default: migration advice
        if "goal" not in self.context:
            self.context["goal"] = user_input
            return "What is your age?"
        elif "age" not in self.context:
            self.context["age"] = user_input
            return "What is your budget in USD?"
        elif "budget" not in self.context:
            self.context["budget"] = user_input
            advisor = MigrationAdvisor(self.llm)
            user_ctx = UserContext(
                name="User",
                goal=self.context["goal"],
                country=self.context.get("country", ""),
                age=self.context["age"],
                budget=self.context["budget"]
            )
            advice = advisor.advise(user_ctx)
            self.context.clear()
            return advice
        else:
            return "Thank you! Ask another question or restart."
    def recommend_links(self):
        country = self.context.get("country", "").lower().replace(" ", "_")
        goal = self.context.get("goal", "").lower()
        sources = TrustedSourceLoader.load(country, goal)  # You’ll write this next
        if not sources:
            return "I couldn’t find trusted sources for that goal and country yet. Would you like me to search online instead?"
        response = "Here are some helpful links:\n"
        for item in sources:
            response += f"- **{item.name}**: {item.description or 'No description'}\n"
            for url in item.urls:
                response += f"  🔗 {url}\n"
        return response