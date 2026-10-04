import os

from langchain_community.vectorstores import FAISS

from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model


def build_vector_store(chunks):
    """
    Builds a FAISS vector store from the provided document chunks using the configured embeddings model.

    Args:
        chunks (List[Document]): List of LangChain Document objects (chunks of text).

    Returns:
        FAISS: A FAISS vector store object containing the indexed chunks.
    """
    embeddings = get_embeddings_model()
    vector_store = FAISS.from_documents(chunks, embedding=embeddings)
    return vector_store

def save_vector_store(vector_store, path:str = config.VECTOR_STORE_PATH) -> None:
    """
    Saves the FAISS vector store to the given local path.

    Args:
        vector_store (FAISS): The FAISS vector store object to save.
        path (str): The directory path where to save the FAISS index.
    """
    if not os.path.exists(path):
        os.makedirs(path)
    vector_store.save_local(path)

def load_vector_store(path: str = config.VECTOR_STORE_PATH):
    """
    Loads a previously saved FAISS vector store from the given local path.

    Args:
        path (str): The directory path from where to load the FAISS index. Defaults to config.VECTOR_STORE_PATH.

    Returns:
        FAISS: The loaded FAISS vector store object.
    """
    return FAISS.load_local(path, embeddings=get_embeddings_model(),allow_dangerous_deserialization=True)
    

def vector_store_exists(path: str = config.VECTOR_STORE_PATH) -> bool:
    
    """
    Checks if the FAISS vector store exists at the given path.
    
    Args:
        path (str): The path to check for the FAISS index directory.

    Returns:
        bool: True if the index file exists at the path, False otherwise.
    """
    # FAISS saves the index as "index.faiss" in the specified directory by convention
    # We write "index.faiss" because FAISS saves its index data in a file with this name by convention, 
    # so checking for or saving to index.faiss lets us know if a valid FAISS index exists in the directory.
    index_file = os.path.join(path, "index.faiss")
    return os.path.exists(index_file)


def get_retriever(vector_store, top_k: int = config.TOP_K_RESULTS):
    """
    Returns a retriever from the given vector store with the specified top_k results.

    Args:
        vector_store: The FAISS vector store object.
        top_k (int): Number of top results to retrieve. Defaults to config.TOP_K_RESULTS.

    Returns:
        retriever: A retriever instance from the vector store.
    """
    return vector_store.as_retriever(search_kwargs={"k": top_k})


def rerank_with_custom_function(documents, reranker, top_n=5):
    """
    Applies a reranker function to the provided documents (retrieved results) and returns the top_n reranked results.

    Args:
        documents (List[Document]): The list of Documents retrieved from the vector store.
        reranker (callable): A function that takes a list of Documents and returns them ordered by relevance.
        top_n (int): The number of top reranked documents to return.

    Returns:
        List[Document]: The top_n reranked documents.
    """
    reranked_docs = reranker(documents)
    return reranked_docs[:top_n]