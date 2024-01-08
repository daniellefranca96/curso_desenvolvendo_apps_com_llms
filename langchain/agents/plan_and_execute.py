from langchain.chains import LLMMathChain
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.agents import AgentExecutor, load_tools
from langchain_core.tools import Tool
from langchain_experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner,
)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv(key="OPENAI_API_KEY")
os.environ["GOOGLE_CSE_ID"] = os.getenv(key="GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv(key="GOOGLE_API_KEY")

tools = load_tools(
    ["arxiv", "google-search"],
)

model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")
model_executor = ChatOpenAI(model="gpt-3.5-turbo-1106")

planner = load_chat_planner(model)
executor = load_agent_executor(model_executor, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor)
print(agent.run("Que dia será a páscoa em 2024?"))

