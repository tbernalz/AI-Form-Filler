import os
from dotenv import load_dotenv

load_dotenv()


CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 200))
OLLAMA_API_URL: str = os.getenv("OLLAMA_API_URL")
LLM_MODEL_NAME: str = os.getenv("LLM_MODEL_NAME")
OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL: str = os.getenv("OPENROUTER_API_URL")


if CHUNK_SIZE <= 0:
    raise ValueError("CHUNK_SIZE must be a positive integer")

if CHUNK_OVERLAP < 0:
    raise ValueError("CHUNK_OVERLAP must be a non-negative integer")
