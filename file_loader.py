from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader
from langchain.document_loaders import TextLoader

def load_documents(file_paths):
    docs = []
    for path in file_paths:
        if path.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif path.endswith(".docx"):
            loader = UnstructuredWordDocumentLoader(path)
        elif path.endswith(".txt"):
            loader = TextLoader(path)
        else:
            continue
        docs.extend(loader.load())
    return docs


