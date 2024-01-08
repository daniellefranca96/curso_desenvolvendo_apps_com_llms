from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

from vertexai.language_models import TextGenerationModel
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "YOUR_CREDENTIALS_FILE.json"
os.environ['GOOGLE_CLOUD_PROJECT'] = "YOUR_PROJECT_NAME"

model = TextGenerationModel.from_pretrained("text-bison@002")

class CustomLLM(LLM):


    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        
        return model.predict(prompt).text


llm = CustomLLM()
print(llm("When was Obama president?"))
