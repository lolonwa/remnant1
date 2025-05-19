from app.services.llm_service import LLMService
from app.utils.prompt_factory import PromptFactory
from app.utils.user_context import UserContext

class MigrationAdvisor:
    """
    Handles logic to advise users on migration paths based on their context.
    This includes study, work, asylum, and other possible routes.
    """

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def advise(self, user_context: UserContext) -> str:
        """
        Use LLM to analyze user context and return migration advice.
        """
        prompt = PromptFactory.migration_prompt(user_context)
        return self.llm_service.query_llm(prompt)