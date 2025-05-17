# scholarship_finder.py - Auto-generated module in remnant/core

"""
Module: scholarship_finder.py
Location: remnant/core
Purpose: Describe the functionality here.
"""


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
