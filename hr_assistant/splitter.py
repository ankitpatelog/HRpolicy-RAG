from langchain_text_splitters import RecursiveCharacterTextSplitter

from hr_assistant import config

def split_into_chunks(documents):
    """
    Splits a list of LangChain Document objects into smaller chunks using
    RecursiveCharacterTextSplitter with the configured chunk size and overlap.

    Args:
        documents (List[Document]): List of Document objects to split.

    Returns:
        List[Document]: List of chunked Document objects.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    # Flatten list of lists into a single list of chunks
    split_docs = []
    for doc in documents:
        split_docs.extend(text_splitter.split_documents([doc]))
    return split_docs