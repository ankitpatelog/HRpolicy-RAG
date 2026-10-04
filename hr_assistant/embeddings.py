from langchain_community.embeddings import JinaEmbeddings

from hr_assistant import config

def get_embeddings_model():
    """
    Returns an instance of the JinaEmbeddings model using the API key from the config.
    """
    return JinaEmbeddings(
        model_name=config.EMBEDDINGS_MODEL_NAME,
        jina_api_key=config.settings.JINA_API_KEY
    )


