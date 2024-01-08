import json
from llama_cpp import Llama
from gmail import GmailAPI
from langchain.chat_models import ChatOpenAI
import os


os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'

def send_ai(prompt):
    chat = ChatOpenAI(model_name="gpt-4-1106-preview")
    return chat.predict(prompt)

llm = Llama(model_path="C:\\Users\\danie\\Documents\\AI\\llama\\models\\gorilla-openfunctions-v1.Q4_K_M.gguf")

gmailapi = GmailAPI()

functions = [
    {
        "name": "send_ai",
        "api_name": "send_ai",
        "description": "useful when you need to answer a question of general knowledge, custom function if other don't apply",
        "parameters":  [
            {"name": "prompt", "description": "what you need to send to the model"},
        ]
    },
    {
        "name": "gmailapi.search_messages",
        "api_name": "gmailapi.search_messages",
        "description": "Search gmail messages using the gmail api",
        "parameters":  [{"name": "query", "description": "a custom gmail query"}, {"name":"max_results", "description": "number of quantity of results to return"}]
    },
    {
        "name": "gmailapi.get_message",
        "api_name": "gmailapi.get_message",
        "description": "Get information about an gmail message",
        "parameters":  [{"name": "msg_id", "description": "the id og the message"}]
    },
    {
        "name": "gmailapi.send_message",
        "api_name": "gmailapi.send_message",
        "description": "Sends a message",
        "parameters":  [
            {"name": "sender", "description": "email of the sender of the message"},
            {"name": "to", "description": "email of the receiver of the message"},
            {"name": "subject", "description": "subject of the message"},
            {"name": "message", "description": "text of the message"}
        ]
    }
]

prompt = "USER: <<question>> {prompt} <<function>> {{function_string}} \nASSISTANT:".replace('{{function_string}}', json.dumps(functions))

#user = "Send a email from daniellefranca96@gmail.com to daniellefranca96@outlook.com with subject 'Test2' and message 'This is a test'"

user = "hi"

prompt = prompt.replace('{prompt}', user)

result = llm(prompt)

print(result['choices'][0]['text'])
print(eval(result['choices'][0]['text']))



 
