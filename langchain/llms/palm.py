from langchain.chat_models import ChatVertexAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from custom_llm import CustomLLM
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "stellar-equator-404020-655c4ba2eb77.json"
os.environ['GOOGLE_CLOUD_PROJECT'] = "stellar-equator-404020"


messages = [
    SystemMessage(
        content="You are a helpful assistant"
    ),
    HumanMessage(
        content="O que é AGI?"
    ),
]

llm = CustomLLM()
print(llm("O que é AGI?"))

#chat = ChatVertexAI(model_name="chat-bison@002")
#print(chat(messages))
