import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

def create_vector_store(texts):
    return FAISS.from_texts(texts, embeddings)

