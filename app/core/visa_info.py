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

    def get_info(self, country, visa_type):
        """
        Retrieve general visa information for a given country and visa type.
        """
        prompt = (
            f"Provide detailed information about {visa_type} visas for {country}. "
            "Include eligibility, required documents, typical processing time, and any tips for applicants."
        )
        return self.llm_service.query_llm(prompt)
