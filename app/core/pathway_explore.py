# core/pathway_explorer.py

"""
Module: pathway_explorer.py
Purpose: Suggests realistic migration pathways (like trade jobs, study, or work) based on user context.
"""

from utils.user_context import UserContext
from app.services.llm_service import LLMService

class PathwayExplorer:
    def __init__(self, llm_service: LLMService):
        self.llm = llm_service

    def explore_paths(self, user_context: UserContext) -> str:
        """
        Uses LLM to suggest viable migration routes based on user's goal, country, and budget.
        """
        prompt = self._build_prompt(user_context)
        return self.llm.ask(prompt)

    def _build_prompt(self, context: UserContext) -> str:
        return f"""
You are a smart migration advisor.

A user wants to migrate with the following profile:
- Goal: {context.goal}
- Country: {context.country}
- Age: {context.age}
- Budget: {context.budget} USD

Suggest 2–3 realistic migration pathways they could explore, especially if they are open to skilled trades or study-work programs.

For each pathway, include:
- Name of the pathway (e.g. "Caregiver visa", "Truck driver trade route")
- Description of what it involves
- Why it’s a good option
- Steps needed to qualify
- Helpful websites (for job listings, visa info, or training)

Respond in structured YAML format.
"""
