from langchain.agents.openai_assistant import OpenAIAssistantRunnable

import os

os.environ['OPENAI_API_KEY']='YOUR_API_KEY'

interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
    name="langchain assistant",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
)
output = interpreter_assistant.invoke({"content": "What's 10 - 4 raised to the 2.7"})
print(output)