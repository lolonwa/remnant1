from app.utils.prompt_factory import PromptFactory

class MigrationAdvisor:
    def __init__(self, llm_service):
        self.llm_service = llm_service

    def advise(self, user_context):
        """
        Builds a structured prompt and sends it to the LLM.
        """
        prompt = PromptFactory.build_migration_prompt(user_context)
        return self.llm_service.query_llm(prompt)
