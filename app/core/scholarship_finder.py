from app.utils.prompt_factory import PromptFactory

class ScholarshipFinder:
    def __init__(self, llm_service):
        self.llm_service = llm_service

    def find(self, country, level):
        """
        Use a structured prompt to query for scholarships.
        """
        prompt = PromptFactory.build_scholarship_prompt(country, level)
        return self.llm_service.query_llm(prompt)
