# migration_advisor.py - Auto-generated module in remnant/core

"""
Module: migration_advisor.py
Location: remnant/core
Purpose: Describe the functionality here.
"""


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
        prompt_type = "admission_advice"
        variables = {
            "country": user_context.country,
            "user_profile": f"Name: {user_context.name}, Goal: {user_context.goal}, Age: {user_context.age}, Budget: {user_context.budget}"
        }
        return self.llm_service.run_prompt(prompt_type, variables)
