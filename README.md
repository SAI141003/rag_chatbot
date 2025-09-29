# 📚 RAG Document Chatbot

## **Description**
The RAG (Retrieval-Augmented Generation) Document Chatbot is an AI-powered tool that allows users to **upload their own documents** (PDF, DOCX, TXT) and interact with a chatbot that answers questions based on the content of those documents. It leverages **vector embeddings** and **lightweight LLMs** to provide fast, context-aware responses without relying on paid APIs.

This project combines **document parsing, vector databases, and a conversational AI interface** into a single, easy-to-use Streamlit app.

---

## **Key Features**
- **Multi-format document upload**: PDF, DOCX, TXT.
- **Document parsing and indexing**: Extracts text from uploaded files and stores it in a vector store.
- **Retrieval-Augmented Generation (RAG)**: Answers questions using the knowledge stored in uploaded documents.
- **Lightweight LLM integration**: Uses small, CPU-friendly models like `FLAN-T5-Small` for offline inference.
- **Interactive chat interface**:
  - Chat bubbles for user and bot messages
  - Timestamps
  - Typing animation for a real-time feel
- **Session persistence**: Stores uploaded files and chat history during the session.
- **Sidebar with document info**: Displays uploaded files and metadata.
- **Frontend styling**: Clean and responsive interface for an engaging user experience.

---

## **Tech Stack**
- **Backend/AI**: Python, LangChain, FAISS vector store, FLAN-T5-Small LLM
- **Frontend**: Streamlit, HTML/CSS for chat styling
- **File Handling**: Python file I/O for uploaded documents

---

## **Installation**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/<USERNAME>/<REPO>.git
   cd rag_chatbot
