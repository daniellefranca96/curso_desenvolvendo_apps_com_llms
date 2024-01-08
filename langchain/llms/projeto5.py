from langchain.prompts import StringPromptTemplate
from pydantic import BaseModel, validator
from langchain.llms import Bedrock
import boto3
import os

PROMPT = """
Generate a titile for an {content} about {description}. Title:
"""
os.environ['AWS_ACCESS_KEY_ID'] = "AWS_ACCESS_KEY_ID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "AWS_SECRET_ACCESS_KEY"

BEDROCK_CLIENT = boto3.client("bedrock-runtime", 'us-east-1')
llm = Bedrock(
    client=BEDROCK_CLIENT, model_id="anthropic.claude-v2",
    model_kwargs={"max_tokens_to_sample": 1000}
)


class GenerateTitlePromptTemplate(StringPromptTemplate, BaseModel):
    """A custom prompt template that generates a title from a content and description."""

    @validator("input_variables")
    def validate_input_variables(cls, v):
        """Validate that the input variables are correct."""
        if len(v) != 2 or "content" not in v or "description" not in v:
            raise ValueError("from_lan, to_lang and input must be provided.")
        return v

    def format(self, **kwargs) -> str:

        # Generate the prompt to be sent to the language model
        prompt = PROMPT.format(
            content=kwargs["content"], description=kwargs["description"]
        )
        return prompt

    def _prompt_type(self):
        return "translate_prompt"
        
        

prompt_template=GenerateTitlePromptTemplate(input_variables=["content", "description"])

print("## GENERATE TITLE: ##")
content = input("type of content: ")
description = input("description: ")
print("title: ")
print(llm(prompt_template.format(content=content, description=description)))

