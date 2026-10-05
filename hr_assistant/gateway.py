# app/llm/gateway.py

from langchain_openai import ChatOpenAI
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

from hr_assistant import config


# ============================================================
# CREATE LLM THROUGH PORTKEY
# ============================================================

def get_gateway_llm() -> ChatOpenAI:
    """
    Create a LangChain ChatOpenAI instance
    connected to the Portkey Gateway.

    Portkey handles the routing using the saved
    configuration referenced by PORTKEY_CONFIG_ID.

    Flow:

        Primary Model
             ↓
          Failure?
             ↓
        Backup Model
    """

    return ChatOpenAI(
        # ====================================================
        # Portkey Gateway
        # ====================================================

        base_url=PORTKEY_GATEWAY_URL,

        # Portkey API key
        api_key=config.settings.PORTKEY_API_KEY,

        # ====================================================
        # Saved Portkey Configuration
        # ====================================================
        #
        # IMPORTANT:
        # Do NOT pass the PORTKEY_CONFIG dictionary here.
        #
        # Your Portkey workspace has:
        #
        # block_inline_config = enabled
        #
        # Therefore we reference the saved config using
        # its pc-xxxxxxxx ID.
        #

        default_headers=createHeaders(
            api_key=config.settings.PORTKEY_API_KEY,
            config=config.settings.PORTKEY_CONFIG_ID,
        ),

        # ====================================================
        # Model
        # ====================================================
        #
        # Required by ChatOpenAI.
        # Actual provider/model routing is controlled
        # by the saved Portkey configuration.
        #

        model=config.LLM_MODEL_NAME,
    )