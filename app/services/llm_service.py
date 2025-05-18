"""
llm_service.py - Provides integration with LLM (e.g., Google Gemini) using LangChain.
This module centralizes all LLM queries using reusable prompt templates and clean interfaces.
"""

import os
from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables (like API key)
load_dotenv()


class PromptFactory:
    """
    Factory class for generating prompt templates.
    This makes the prompts easy to manage and reuse across the app.
    """

    @staticmethod
    def get_prompt(prompt_type: str) -> PromptTemplate:
        """
        Returns a LangChain PromptTemplate based on the type of request.
        Extend this method to add more prompts like admission, visa, jobs, etc.
        """
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
                    "Respond with structured YAML like this:\n"
                    "```yaml\n"
                    "universities:\n"
                    "  - name: University of XYZ\n"
                    "    tuition: 12000 USD/year\n"
                    "    start_date: September 2025\n"
                    "    requirements:\n"
                    "      - IELTS 6.5\n"
                    "      - Bachelors in related field\n"
                    "recommendation: string\n"
                    "advice: string\n"
                    "```\n"
                )
            )

        raise ValueError(f"No prompt defined for type: {prompt_type}")


class LLMService:
    """
    Service class that handles all LLM interactions.
    Follows dependency inversion by exposing a simple, high-level interface.
    """

    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Google API Key not found! Make sure it's set in your .env file.")

        # self.llm = ChatGoogleGenerativeAI(
        #     model="llama3.2:latest",
        #     temperature=0.7,
        #     google_api_key=api_key
        # )
        self.llm = ChatOllama(
            model="llama3.2:latest",
            temperature=0.7,
            api_key=api_key
        )
    def run_prompt(self, prompt_type: str, variables: dict) -> str:
        """
        Execute a query using a named prompt and input variables.

        :param prompt_type: The type of prompt to use (e.g., scam_detection, admission_advice).
        :param variables: A dictionary of variables needed by the prompt.
        :return: The LLM response as a string (can be YAML or natural text).
        """
        prompt = PromptFactory.get_prompt(prompt_type)
        chain = LLMChain(llm=self.llm, prompt=prompt, verbose=True)
        return chain.run(variables)
