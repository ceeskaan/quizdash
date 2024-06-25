import os
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Any LLM (Groq and Ollama should also work)
llm = ChatOpenAI(
    model_name="databricks-dbrx-instruct", 
    openai_api_key="123", #os.getenv("DBRX_API_KEY")
    openai_api_base="123", #os.getenv("DBRX_BASE_URL")
)







