from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents import AgentExecutor, load_tools
import os

os.environ['OPENAI_API_KEY']='YOUR_API_KEY'

tools = load_tools(
    ["arxiv"],
)


agent = OpenAIAssistantRunnable.create_assistant(
    name="langchain",
    instructions="You are a helpfull assistant.",
    tools=tools,
    model="gpt-4-1106-preview",
    as_agent=True,
)

agent_executor = AgentExecutor(agent=agent, tools=tools)

print(agent_executor.invoke({"content": "What is the paper 2312.01479v5 about?"}))
