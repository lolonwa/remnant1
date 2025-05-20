from app.utils.prompt_factory import PromptFactory

class VisaInfoAdvisor:
    def __init__(self, llm_service):
        self.llm_service = llm_service

    def get_requirements(self, country, purpose):
        """
        Use a structured prompt to retrieve visa requirements.
        """
        prompt = PromptFactory.build_visa_prompt(country, purpose)
        return self.llm_service.query_llm(prompt)
