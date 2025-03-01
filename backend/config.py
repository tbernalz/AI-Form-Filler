import os
from dotenv import load_dotenv

load_dotenv()


CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 200))
OLLAMA_API_URL: str = os.getenv("OLLAMA_API_URL")
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL")

if CHUNK_SIZE <= 0:
    raise ValueError("CHUNK_SIZE must be a positive integer")

if CHUNK_OVERLAP < 0:
    raise ValueError("CHUNK_OVERLAP must be a non-negative integer")
