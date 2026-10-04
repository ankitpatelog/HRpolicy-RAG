import os

from dotenv import load_dotenv
load_dotenv()

# settings class for api keys
class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    JINA_API_KEY = os.getenv("JINA_API_KEY")

settings = Settings()

# Define path - data/ vectorstore/

DATA_FILE_PATH = os.path.join("data","policy.txt")

VECTOR_STORE_PATH = os.path.join("data","faiss_index")

# models
# llm and embeddings models

LLM_MODEL_NAME = "openai/gpt-oss-120b"

EMBEDDINGS_MODEL_NAME = "jina-embeddings-v2-base-en"

# chunk/ text splitting config

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# RETRIEVAL CONFIG

TOP_K_RESULTS = 5


# SYSTEM INSTRUCTIONS

SYSTEM_PROMPT = (
    """
    You are a helpful assistant that can answer questions about the company policy.
    You are given a question and a context.
    You need to answer the question based on the context.
    If you don't know the answer, you should say "I don't know".
    If you know the answer, you should answer the question.
    If you don't know the answer, you should say "I don't know".
    You should use the context to answer the question.
    You should not use the context to answer the question if it is not relevant.
    You should not use the context to answer the question if it is not helpful.
    You should not use the context to answer the question if it is not correct.
    You should not use the context to answer the question if it is not complete.
    You should not use the context to answer the question if it is not accurate.
    You should not use the context to answer the question if it is not up to date.
    """
)



def check_api_keys():
    """
    check if the api keys are set or not
    """

    if not settings.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set")
    if not settings.JINA_API_KEY:
        raise ValueError("JINA_API_KEY is not set")