"""
# ex1 communication with LLM

"""

# Import necessary libraries
from langchain_openai import ChatOpenAI
import os
import dotenv
# Load environment variables from .env file
dotenv.load_dotenv()


llm = ChatOpenAI(
        model=  os.getenv("OPENAI_MODEL"),
        api_key= os.getenv("OPENAI_API_KEY")
        )

# Invoke the chain

prompt =  input("Give me your question") 
response = llm.invoke( prompt)
print(response.content)   