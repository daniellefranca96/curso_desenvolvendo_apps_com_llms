from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent, load_tools
from langchain.memory import ConversationBufferMemory
from langchain import hub
import os

os.environ['OPENAI_API_KEY']='YOUR_API_KEY'

prompt = hub.pull("stepbystep/conversational-agent")

memory = ConversationBufferMemory(memory_key="chat_history")

llm = ChatOpenAI(model='gpt-4')

tools = load_tools(
    ["arxiv"],
)

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True, memory=memory)

print(agent_executor.invoke({"input": "what is this paper 2312.16862v1 about?"}))
print(agent_executor.invoke({"input": "Number of TinyGPT paper?"}))
