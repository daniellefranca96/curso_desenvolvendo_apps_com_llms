from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import os

os.environ['OPENAI_API_KEY']='YOUR_API_KEY'

api_key='YOUR_API_KEY'

client = OpenAI(api_key=api_key)

file = client.files.create(
  file=open("2312.16862v1.pdf", "rb"),
  purpose='assistants'
)

assistant = client.beta.assistants.create(
  instructions="You are a helpfull assistant.",
  model="gpt-4-1106-preview",
  tools=[{"type":"retrieval"}],
  file_ids=[file.id]
)

print(str(assistant))

agent = OpenAIAssistantRunnable(assistant_id=assistant.id, as_agent=True)
print(agent.invoke({"content": "O que é TinyGPT-V"}))