# connect to the llm 

from langchain_groq import ChatGroq
from hr_assistant import config

from hr_assistant import gateway

def get_llm():
    return gateway.get_gateway_llm()

# user->gateway->llm