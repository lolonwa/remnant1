from app.services.llm_service import LLMService
from app.utils.prompt_factory import PromptFactory

class ScamDetector:
    """
    Detects potential scam or fake job/visa offers using LLM analysis.
    """

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def analyze_offer(self, text: str) -> str:
        """
        Analyze a given job or visa offer for red flags.
        """
        prompt = PromptFactory.scam_prompt(text)
        return self.llm_service.query_llm(prompt)