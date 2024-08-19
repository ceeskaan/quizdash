import os
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# DBRX LLM
llm = ChatOpenAI(
    model_name="databricks-dbrx-instruct", 
    openai_api_key=os.getenv("DBRX_API_KEY"),
    openai_api_base=os.getenv("DBRX_BASE_URL")
)







