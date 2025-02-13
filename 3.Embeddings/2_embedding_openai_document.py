from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

document = [
    'Dehli is the capital of India',
    'Islambad is the capital of Pakistan',
    'Paris is the capital of France'
]

embedding= OpenAIEmbeddings(model='text-embedding-3-large', dimension=32)

result = embedding.embed_documents(document)

print(str(result))