# visa_info.py - Auto-generated module in remnant/core

"""
Module: visa_info.py
Location: remnant/core
Purpose: Describe the functionality here.
"""


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
