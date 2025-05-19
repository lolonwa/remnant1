# remnant/config.py

import os

# API keys and config loaded from environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "")

# Select which LLM provider to use: "openrouter" or "ollama"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openrouter")
