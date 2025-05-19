"""
LLMService handles all interactions with language models.
Supports OpenRouter (LLaMA 3.3) and can easily be switched back to Ollama.
"""

# from openai import OpenAI  # Uncomment if using Ollama/OpenAI SDK for local models
import os
from openai import OpenAI
import dotenv 
from app.utils.prompt_factory import PromptFactory

load_dotenv()  # Load environment variables from .env file
class LLMService:
    """
    LLMService routes prompts to OpenRouter's API (LLaMA 3.3 for now).
    You can switch back to Ollama by uncommenting the appropriate lines.
    """

    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
        self.model = "meta-llama/llama-3.3-8b-instruct:free"

    def query_llm(self, prompt: str) -> str:
        """
        Sends a prompt to the LLM and returns the raw text response.
        """
        try:
            response = self.client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://yourdomain.com",  # Optional
                    "X-Title": "Remnant Migration App"         # Optional
                },
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[ERROR] Failed to get LLM response: {e}"


# --- Ollama Example (if switching back) ---
# from openai import OpenAI
# client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
# model = "llama3"
# Replace the client/model above to re-enable Ollama
