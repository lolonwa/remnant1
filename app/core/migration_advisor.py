# migration_advisor.py
from app.utils.prompt_factory import PromptFactory
from app.services.llm_service import LLMService
from app.utils.user_context import UserContext
class MigrationAdvisor:
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def advise(self, user_context: UserContext):
        prompt = PromptFactory.build_migration_advice_prompt(user_context.to_dict())
        return self.llm_service.query_llm(prompt)
