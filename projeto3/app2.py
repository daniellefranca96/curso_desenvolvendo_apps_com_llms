import chainlit as cl
from gmail import GmailAPI
from functions import functions
from langchain.agents import AgentType, initialize_agent
from langchain.tools import StructuredTool
from langchain.chat_models import ChatOpenAI
import json
import os

os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'

gmailapi = GmailAPI()

functions_map = {"SearchEmailMessages": gmailapi.search_messages, "GetMessage":gmailapi.get_message, "SendMessage": gmailapi.send_message, "DeleteMessage":gmailapi.delete_message}

messages = []

llm = ChatOpenAI(model_name="gpt-4-1106-preview")

tools = [
    StructuredTool.from_function(
        name="SearchEmailMessages",
        func=gmailapi.search_messages,
        description="useful for when you need search emails, receives a custom gmail query as input",
    ),
    StructuredTool.from_function(
        name="GetMessage",
        func=gmailapi.get_message,
        description="useful for when you need get all info about an specific email, receives email_id as input",
    ),
    StructuredTool.from_function(
        name="SendMessage",
        func=gmailapi.send_message,
        description="useful for when you need send an message, receives sender: str, to: str, subject: str, message: str as input",
    )
]

agent_executor = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True
)

@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from Tool 1, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """
    
    response = agent_executor.invoke({"input": message.content})
    
    # Send the final answer.
    await cl.Message(content=response['output']).send()
    
   
   