# app/interface/streamlit/chat_manager.py

from app.services.llm_service import LLMService
from utils.user_context import UserContext

class ChatManager:
    def __init__(self):
        self.state = {
            "name": None,
            "goal": None,
            "country": None,
            "age": None,
            "budget": None,
            "step": 0,
        }
        self.llm = LLMService()

    def handle_user_input(self, user_input):
        # Route user through steps
        step = self.state["step"]

        if step == 0:
            self.state["name"] = user_input
            self.state["step"] += 1
            return "Hi " + user_input + "! What is your migration goal? (study / work / asylum)"

        elif step == 1:
            self.state["goal"] = user_input.lower()
            self.state["step"] += 1
            return f"Great. Which country are you considering for {self.state['goal']}?"

        elif step == 2:
            self.state["country"] = user_input
            self.state["step"] += 1
            return "What is your age?"

        elif step == 3:
            self.state["age"] = user_input
            self.state["step"] += 1
            return "What is your budget in USD?"

        elif step == 4:
            self.state["budget"] = user_input
            self.state["step"] += 1
            return self._generate_advice()

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
        response = self.llm.get_advice(context)
        return f"Here is your personalized advice:\n\n{response}"
