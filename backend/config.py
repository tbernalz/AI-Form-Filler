import os


CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 200))

if CHUNK_SIZE <= 0:
    raise ValueError("CHUNK_SIZE must be a positive integer")

if CHUNK_OVERLAP < 0:
    raise ValueError("CHUNK_OVERLAP must be a non-negative integer")
