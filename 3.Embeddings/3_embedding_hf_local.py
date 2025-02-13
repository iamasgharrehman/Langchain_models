from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Islamabad is Capital of Pakistan"

result = embedding.embed_query(text)

print(str(result))