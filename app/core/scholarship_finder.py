from app.services.llm_service import LLMService
from app.utils.prompt_factory import PromptFactory

class ScholarshipFinder:
    """
    Finds scholarship information using LLM search.
    """

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def find(self, country: str, level: str) -> str:
        """
        Query scholarships based on country and level of study.
        """
        prompt = PromptFactory.scholarship_prompt(country, level)
        return self.llm_service.query_llm(prompt)