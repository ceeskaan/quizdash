import os

from langchain_groq import ChatGroq

from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Any LLM 
llm = ChatGroq(
    api_key = os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"
)







