import os
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
sec_key = os.getenv("HF_TOKEN")

# 1. Define the specific Model URL (We bypass the "search" step)
# This URL is the standard address for the TinyLlama model on Hugging Face
model_url = "https://api-inference.huggingface.co/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# 2. Configure the LLM using endpoint_url
llm = HuggingFaceEndpoint(
    endpoint_url=model_url,  # <--- THIS IS THE KEY FIX
    task="text-generation",
    huggingfacehub_api_token=sec_key
)

print("--- Sending Request ---")

try:
    # 3. Invoke
    result = llm.invoke("Who is the Prime Minister of India?")
    print("✅ Success!")
    print(result)
except Exception as e:
    print(f"❌ Error: {e}")