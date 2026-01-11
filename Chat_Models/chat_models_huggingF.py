import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("HF_TOKEN not found in .env file")

print("--- Using HuggingFace Inference API (Conversational) ---\n")

# Create inference client
client = InferenceClient(api_key=hf_token)

# These models support conversational task
models_to_try = [
    "HuggingFaceH4/zephyr-7b-beta",
    "mistralai/Mistral-7B-Instruct-v0.1",
    "tiiuae/falcon-7b-instruct",
    "meta-llama/Llama-2-7b-chat-hf",
]

prompt = "Who is the Prime Minister of India?"
success = False

for model in models_to_try:
    try:
        print(f"Trying: {model}")
        
        # Use conversational method instead of text_generation
        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            model=model,
            max_tokens=200
        )
        
        # Extract the response text
        answer = response.choices[0].message.content
        
        print(f"✅ SUCCESS!\n")
        print(f"Model: {model}")
        print(f"Question: {prompt}")
        print(f"Answer: {answer}\n")
        success = True
        break
        
    except Exception as e:
        error_msg = str(e)[:150]
        print(f"❌ Failed: {error_msg}\n")
        continue

if not success:
    print("\n⚠️ All models failed. Troubleshooting steps:")
    print("1. Check your internet connection")
    print("2. Verify HF_TOKEN is valid: https://huggingface.co/settings/tokens")
    print("3. Make sure your HF account has access to these models")
    print("4. Wait a moment (API might be rate limited or overloaded)")
    print("5. Try this in browser to test: https://huggingface.co/chat")