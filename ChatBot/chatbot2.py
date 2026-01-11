from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()



# Load API key from environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in environment. Add it to your .env file.")
    raise SystemExit(1)

# Instantiate the model with required 'model' parameter and API key
try:
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.0,
        google_api_key=api_key,
    )
except Exception as e:
    print(f"Failed to create ChatGoogleGenerativeAI: {e}")
    raise

chat_history = []
def main():
    print("Type a message and press Enter. Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("You: ")
        chat_history.append({"role": "user", "content": user_input})
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break

        try:
            # The model may accept a string or a list of messages depending on version
            response = model.invoke(chat_history)
            chat_history.append({"role": "assistant", "content": getattr(response, 'content', response)})
            print(f"AI: {getattr(response, 'content', response)}")
        except Exception as e:
            print(f"An error occurred when calling the model: {e}")
        


    


if __name__ == "__main__":
    main()

