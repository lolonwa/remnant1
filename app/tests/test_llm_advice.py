"""
llm_service.py - Handles interaction with LLMs (OpenRouter or Ollama).

This module provides an abstraction layer over different LLM providers.
You can switch between OpenRouter (cloud) and Ollama (local) by commenting/uncommenting as needed.

📁 Location: migration_app/llm/llm_service.py
"""

import os
from dotenv import load_dotenv

# ==== LLM Client: OpenRouter ====
from openai import OpenAI

# ==== LangChain PromptTemplate ====
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import HumanMessage

# ==== (Optional) Ollama Client ====
# from langchain_ollama import ChatOllama

# Load environment variables (.env file)
load_dotenv()


class PromptFactory:
    """
    Generates reusable prompt templates for different tasks.
    """

    @staticmethod
    def get_prompt(prompt_type: str) -> PromptTemplate:
        if prompt_type == "scam_detection":
            return PromptTemplate(
                input_variables=["message"],
                template=(
                    "You are a scam detection assistant. Analyze the following message and decide if it's a "
                    "scam, phishing attempt, or safe. Be detailed but easy to understand.\n\n"
                    "Message:\n\"\"\"\n{message}\n\"\"\"\n\n"
                    "🧠 Analysis:\n"
                    "- Scam or Not:\n"
                    "- Reason:\n"
                    "- Advice for user:"
                )
            )

        elif prompt_type == "admission_advice":
            return PromptTemplate(
                input_variables=["country", "user_profile"],
                template=(
                    "You are an expert admission advisor. A user wants to study in {country}.\n"
                    "Here is their profile: {user_profile}\n\n"
                    "Respond in clear and helpful paragraphs."
                )
            )

        raise ValueError(f"No prompt defined for type: {prompt_type}")


class LLMService:
    """
    Handles interaction with OpenRouter or Ollama (comment/uncomment to switch backend).
    """

    def __init__(self):
        self.provider = "openrouter"  # Can be 'openrouter' or 'ollama'

        if self.provider == "openrouter":
            # ✅ OpenRouter (Cloud LLM via OpenAI-style API)
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENROUTER_API_KEY")
            )

        # ==== Optional Local Ollama LLM ====
        # elif self.provider == "ollama":
        #     self.client = ChatOllama(
        #         model="llama3.2:latest",
        #         temperature=0.7
        #     )

    def run_prompt(self, prompt_type: str, variables: dict) -> str:
        """
        Executes the appropriate LLM prompt using OpenRouter or Ollama.

        :param prompt_type: e.g., "scam_detection", "admission_advice"
        :param variables: dict with required prompt variables
        :return: LLM string response
        """
        prompt = PromptFactory.get_prompt(prompt_type)
        formatted_prompt = prompt.format(**variables)

        if self.provider == "openrouter":
            # Compose the chat message
            response = self.client.chat.completions.create(
                model="meta-llama/llama-3.3-8b-instruct:free",
                messages=[{"role": "user", "content": formatted_prompt}],
                extra_headers={
                    "HTTP-Referer": "<YOUR_SITE_URL>",
                    "X-Title": "<YOUR_SITE_NAME>"
                }
            )
            return response.choices[0].message.content.strip()

        # ==== Optional Local Ollama Integration ====
        # elif self.provider == "ollama":
        #     chain = LLMChain(llm=self.client, prompt=prompt, verbose=True)
        #     return chain.run(variables)

        raise ValueError("Unsupported LLM provider configured.")


# Example usage
if __name__ == "__main__":
    # Run a test prompt
    llm = LLMService()
    result = llm.run_prompt("scam_detection", {"message": "You won a free visa, click here!"})
    print("\n--- Scam Detection Result ---")
    print(result)
