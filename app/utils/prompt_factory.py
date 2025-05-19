"""
PromptFactory helps format consistent prompts for different use cases.
"""

class PromptFactory:
    @staticmethod
    def migration_advice_prompt(user_context) -> str:
        return f"What is the best migration option for: {user_context}?"

    @staticmethod
    def scam_check_prompt(text: str) -> str:
        return f"Is this a scam? Analyze this offer: {text}"

    @staticmethod
    def scholarship_prompt(country: str, level: str) -> str:
        return f"Find scholarships in {country} for {level} level."

    @staticmethod
    def visa_prompt(country: str, purpose: str) -> str:
        return f"What are the visa requirements for {country} for {purpose}?"
