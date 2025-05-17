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
        prompt = f"What is the best migration option for: {user_context}?"
        return self.llm_service.query_llm(prompt)
