from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()
model  = ChatOpenAI(model='gpt-3.5-turbo-instruct')

result = model.invoke("who is the prime minister of india")
print(result.content) 