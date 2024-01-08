import chainlit as cl
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents import AgentExecutor, load_tools, create_openai_functions_agent
from langchain_core.tools import Tool
from langchain_experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner,
)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from tempfile import TemporaryDirectory
from langchain import hub
import pathlib

from langchain_community.agent_toolkits import FileManagementToolkit

# We'll make a temporary directory to avoid clutter
workplacedir = str(pathlib.Path(__file__).parent.resolve())+"//workplace"
working_directory = TemporaryDirectory()

toolkit = FileManagementToolkit(
    root_dir=str(workplacedir)
)  


load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv(key="OPENAI_API_KEY")
os.environ["GOOGLE_CSE_ID"] = os.getenv(key="GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv(key="GOOGLE_API_KEY")

tools = load_tools(
    ["dalle-image-generator", "google-search"],
)
tools = tools + toolkit.get_tools()

prompt = hub.pull("hwchase17/openai-functions-agent")

llm = ChatOpenAI(model='gpt-4-1106-preview')

system_prompt = "You are a creative assistant with a lot of creative toosl avalibale, the user will ask to you to generate reports on stories, do as he asks and use your tools to fulfiil their request. You must think step by step and creatively to make decisions without asking feedback for the user while creating reports"

agent = create_openai_functions_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):

    msg = cl.Message(content="")
    await msg.send()
    
    
    response = await agent_executor.ainvoke({"input":system_prompt+"\n\nUser:"+message.content})
    msg.content = response["output"]
    
    # Send the final answer.
    await msg.update()

