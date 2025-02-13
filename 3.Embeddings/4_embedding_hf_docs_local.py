from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

document = ["Islamabad is Capital of Pakistan",
            'Dehli is capital of India',
            'Paris is capital of France']

vector = embedding.embed_documents(document)

print(str(vector))