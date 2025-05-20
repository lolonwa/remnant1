from app.utils.prompt_factory import PromptFactory

class ScamDetector:
    def __init__(self, llm_service):
        self.llm_service = llm_service

    def analyze_offer(self, offer_text):
        """
        Analyze a given job or visa offer using a structured scam detection prompt.
        """
        prompt = PromptFactory.build_scam_prompt(offer_text)
        return self.llm_service.query_llm(prompt)
