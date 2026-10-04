from langchain.tools import tool


def create_search_tool(retriever):

    @tool
    def search_hr_policy(question: str) -> str:
        """
        Search the HR policy knowledge base for answers related to the
        given question.

        Args:
            question: The user's question about HR policy.

        Returns:
            Relevant HR policy information.
        """

        matching_chunks = retriever.invoke(question)

        if not matching_chunks:
            return "No relevant HR policy information found."

        if isinstance(matching_chunks, list):
            return "\n\n".join(
                str(chunk.page_content)
                for chunk in matching_chunks
            )

        return str(matching_chunks)

    return search_hr_policy