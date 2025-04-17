from dotenv import load_dotenv
import os
import openai

load_dotenv()  # This loads variables from .env into environment

openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
print("API Base:", openai.api_base)