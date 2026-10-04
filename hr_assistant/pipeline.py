from hr_assistant import agent, config, document_loader
from hr_assistant.splitter import split_into_chunks
from hr_assistant.vector_store import (
    build_vector_store,
    load_vector_store,
    save_vector_store,
    vector_store_exists,
)


def build_vector_store_for_document(
    filepath: str = config.DATA_FILE_PATH
):
    if vector_store_exists():
        print("Vector store already exists.")
        return load_vector_store()

    print("Vector store is being created from scratch.")

    documents = document_loader.load_documents(filepath)

    chunks = split_into_chunks(documents)

    print(f"Documents loaded and split into {len(chunks)} chunks.")

    vector_store = build_vector_store(chunks)

    save_vector_store(vector_store)

    print("Vector store built successfully.")

    return vector_store


def build_hr_assistant(
    filepath: str = config.DATA_FILE_PATH
):
    config.check_api_keys()

    build_vector_store_for_document(filepath)

    hr_agent = agent.create_hr_assistant_agent()

    return hr_agent


def ask(agent, question: str) -> str:

    response = agent.invoke({
        "input": question
    })

    return response["output"]