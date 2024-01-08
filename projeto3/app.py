import chainlit as cl
from gmail import GmailAPI
from functions import functions
from openai import OpenAI
import json

api_key='YOUR_API_KEY'

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=api_key,
)

gmailapi = GmailAPI()

functions_map = {"SearchEmailMessages": gmailapi.search_messages, "GetMessage":gmailapi.get_message, "SendMessage": gmailapi.send_message, "DeleteMessage":gmailapi.delete_message}

messages = []

def send_ai():
        
    response = chat_completion = client.chat.completions.create(
        messages=messages,
        tools=functions,
        tool_choice="auto",
        model="gpt-4-1106-preview",
        timeout=5000
    )
    
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    messages.append(response_message)

    if tool_calls:
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = functions_map[function_name]
            function_args = json.loads(tool_call.function.arguments)
            returned = function_to_call(**function_args)
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": json.dumps(returned),
                }
            )
            
        return send_ai()
    return response_message


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
    
    
    messages.append({
            "role": "user",
            "content": message.content,
        })
    
    response = send_ai()
    print(response)
    
    # Send the final answer.
    await cl.Message(content=response.content).send()
    
   
   