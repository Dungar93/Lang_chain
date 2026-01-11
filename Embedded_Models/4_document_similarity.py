from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
vectors = embedding.embed_documents(documents)
query = "What is the capital of India?"
query_vector = embedding.embed_query(query)
similarities = cosine_similarity([query_vector], vectors)
most_similar_index = np.argmax(similarities)
print(f"The most similar document to the query '{query}' is: '{documents[most_similar_index]}'")
