from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Use a small CPU-friendly embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vector_store(documents):
    texts = [doc.page_content for doc in documents]
    vector_store = FAISS.from_texts(texts, embedding_model)
    return vector_store
