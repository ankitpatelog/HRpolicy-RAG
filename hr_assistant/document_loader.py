import os

from langchain_community.document_loaders import TextLoader
from pydantic import FilePath
from hr_assistant import config


from typing import List
from langchain_core.documents import Document

from logger import logger

def load_documents(file_path: str = config.DATA_FILE_PATH) -> List[Document]:
    """
    Loads the specified text file and returns its contents as a list of LangChain Document objects.

    Args:
        file_path (str): Path to the text file to be loaded. Defaults to config.DATA_FILE_PATH.

    Returns:
        List[Document]: List of Document objects containing the contents of the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the loaded document list is empty.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    logger.info("Text Loader started")
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.lo4ad()
    
    if not documents:
        raise ValueError(f"No documents were loaded from {file_path}.")

    return documents
    

    