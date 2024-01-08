import json
import boto3
import os


bedrock = boto3.client('bedrock-runtime', 
                        'us-east-1', 
                        endpoint_url="https://bedrock-runtime.us-east-1.amazonaws.com",  # <- Add this to solve (not recognized by the service.)
                        aws_access_key_id="AWS_ACCESS_KEY_ID",
                        aws_secret_access_key="AWS_SECRET_ACCESS_KEY",
                        )

modelId = 'anthropic.claude-v2'
accept = 'application/json'
contentType = 'application/json'

# NOTE: Body must same as following style
prompt = "What is AGI?"
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
print(response_body.get('completion'))