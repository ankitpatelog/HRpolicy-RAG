from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from hr_assistant.config import SYSTEM_PROMPT
from hr_assistant.llm import get_llm
from hr_assistant.tools import create_search_tool
from hr_assistant.vector_store import get_retriever, load_vector_store


def create_hr_assistant_agent():

    vector_store = load_vector_store()

    retriever = get_retriever(vector_store)

    tools = [create_search_tool(retriever)]

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )

    return executor