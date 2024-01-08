import chainlit as cl
import json
import boto3


bedrock = boto3.client('bedrock-runtime', 
                        'us-east-1', 
                        endpoint_url="https://bedrock-runtime.us-east-1.amazonaws.com",  # <- Add this to solve (not recognized by the service.)
                        aws_access_key_id="aws_access_key_id",
                        aws_secret_access_key="aws_secret_access_key",
                        )

modelId = 'anthropic.claude-v2'
accept = 'application/json'
contentType = 'application/json'

messages = []


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
            "human": message.content,
        })
        
    prompt = "\nHistórico do Chat: [{history}]".replace("{history}", str(messages))+"\n "+message.content

    claude_prompt = f"\n\nHuman:{prompt}\n\nAssistant:"
    body = json.dumps({
                "prompt": claude_prompt,
                "temperature": 0.5,
                "top_p": 1,
                "top_k": 250,
                "max_tokens_to_sample": 200,
                "stop_sequences": ["\n\nHuman:"]
                })
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    
    messages.append({
            "assistant": response_body.get('completion')
        })

    
    # Send the final answer.
    await cl.Message(content=response_body.get('completion')).send()