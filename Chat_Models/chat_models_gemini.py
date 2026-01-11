from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize the model with a CURRENT model name
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # This is the current stable standard
    temperature=0
)
# Invoke the model
try:
    result = model.invoke("Who is the Prime Minister of India?")
    print(result.content)
except Exception as e:
    print(f"An error occurred: {e}")