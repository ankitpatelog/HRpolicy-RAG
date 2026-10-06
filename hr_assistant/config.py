import os

from dotenv import load_dotenv

load_dotenv()


# ============================================================
# SETTINGS CLASS FOR API KEYS
# ============================================================

class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    JINA_API_KEY = os.getenv("JINA_API_KEY")

    # Portkey
    PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    PORTKEY_CONFIG_ID = os.getenv("PORTKEY_C ONFIG_ID")


settings = Settings()


# ============================================================
# PATH CONFIGURATION
# ============================================================

DATA_FILE_PATH = os.path.join("data", "policy.txt")

VECTOR_STORE_PATH = os.path.join("data", "faiss_index")


# ============================================================
# MODEL CONFIGURATION
# ============================================================

LLM_MODEL_NAME = "openai/gpt-oss-120b"

EMBEDDINGS_MODEL_NAME = "jina-embeddings-v2-base-en"


# ============================================================
# CHUNK / TEXT SPLITTING CONFIG
# ============================================================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


# ============================================================
# RETRIEVAL CONFIG
# ============================================================

TOP_K_RESULTS = 5


# ============================================================
# SYSTEM INSTRUCTIONS
# ============================================================

SYSTEM_PROMPT = """
You are a helpful assistant that can answer questions about the company policy.

You are given a question and a context.

You must answer the question based on the provided context.

If you don't know the answer, say:
"I don't know."

Rules:

1. Use the provided context to answer the question.
2. Do not use unrelated context.
3. Do not make up information.
4. Do not rely on your own knowledge when the answer is not present in the context.
5. If the context is insufficient, say "I don't know."
6. Give accurate and concise answers.
7. If the context contains the answer, answer directly.
"""


# ============================================================
# LANGSMITH TRACING
# ============================================================

LANGSMITH_TRACING = (
    os.getenv("LANGSMITH_TRACING", "false").lower() == "true"
)

LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")

LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

LANGSMITH_PROJECT = os.getenv(
    "LANGSMITH_PROJECT",
    "default"
)


# ============================================================
# API KEY VALIDATION
# ============================================================

def check_api_keys():
    """
    Check whether required API keys/configuration are set.
    """

    if not settings.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set")

    if not settings.JINA_API_KEY:
        raise ValueError("JINA_API_KEY is not set")

    if not settings.PORTKEY_API_KEY:
        raise ValueError("PORTKEY_API_KEY is not set")

    if not settings.PORTKEY_CONFIG_ID:
        raise ValueError("PORTKEY_CONFIG_ID is not set")