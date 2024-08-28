import os
from dotenv import load_dotenv, find_dotenv

from langchain_groq import ChatGroq

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

llm = ChatGroq(
    api_key = os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"
)







