from langchain.prompts import StringPromptTemplate
from pydantic import BaseModel, validator

PROMPT = """
Translate from {from_lang} to {to_lang} this phrase: {input}
"""


class TranslatePromptTemplate(StringPromptTemplate, BaseModel):
    """A custom prompt template that original language, translation language and phrase and formats the prompt template to provide the translation."""

    @validator("input_variables")
    def validate_input_variables(cls, v):
        """Validate that the input variables are correct."""
        if len(v) != 3 or "from_lang" not in v or "to_lang" not in v  or "input" not in v:
            raise ValueError("from_lan, to_lang and input must be provided.")
        return v

    def format(self, **kwargs) -> str:

        # Generate the prompt to be sent to the language model
        prompt = PROMPT.format(
            from_lang=kwargs["from_lang"], to_lang=kwargs["to_lang"], input=kwargs["input"]
        )
        return prompt

    def _prompt_type(self):
        return "translate_prompt"