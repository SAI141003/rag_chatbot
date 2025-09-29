import streamlit as st
from datetime import datetime
import time
from file_loader import load_documents
from vector_store import create_vector_store
from chat_chain import create_qa_chain

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("📚 RAG Document Chatbot")
st.markdown("Upload your documents and chat with the bot. Answers are based on the content of your files!")

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("Instructions")
    st.markdown("""
    1. Upload PDF, DOCX, or TXT files.
    2. Wait for processing.
    3. Ask questions in the chat box.
    """)
    st.markdown("---")
    st.header("Uploaded Files")
    if "uploaded_files" in st.session_state:
        for f in st.session_state.uploaded_files:
            st.markdown(f"- {f.name}")

# ---------------- File Upload ----------------
uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    st.session_state.uploaded_files = uploaded_files
    file_paths = []
    with st.spinner("Loading documents..."):
        for uploaded_file in uploaded_files:
            path = f"uploaded_{uploaded_file.name}"
            with open(path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            file_paths.append(path)

        # Load documents, create vector store & QA chain
        documents = load_documents(file_paths)
        vector_store = create_vector_store(documents)
        qa_chain = create_qa_chain(vector_store)
    st.success("✅ Documents loaded successfully!")

# ---------------- Chat Interface ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if uploaded_files and qa_chain:
    st.subheader("💬 Chat with your documents")
    col1, col2 = st.columns([1, 2])

    # Left panel: document info
    with col1:
        st.markdown("### 📄 Document Info")
        for doc in documents:
            source = doc.metadata.get("source", "Unknown")
            st.markdown(f"**{source}**")
            st.markdown(f"Characters: {len(doc.page_content)}")
            st.markdown("---")

    # Right panel: chat
    with col2:
        user_question = st.text_input("Type your question:", key="input")
        send_button = st.button("Send")

        chat_box = st.empty()           # Placeholder for chat messages
        typing_placeholder = st.empty() # Placeholder for typing indicator

        if send_button and user_question.strip() != "":
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Show typing animation
            typing_placeholder.markdown("<i>Bot is typing...</i>", unsafe_allow_html=True)
            time.sleep(1)  # simulate typing delay
            answer = qa_chain.run(user_question)
            st.session_state.chat_history.append({
                "user": user_question,
                "bot": answer,
                "time": timestamp
            })
            st.session_state.input = ""
            typing_placeholder.empty()  # Remove typing message

        # Display chat history in scrollable container
        chat_html = "<div style='height:500px; overflow-y:auto; padding:10px; border:1px solid #ddd; border-radius:10px;'>"
        for msg in st.session_state.chat_history:
            # User message
            chat_html += f"""
            <div style="background-color:#DCF8C6; padding:10px; border-radius:10px; margin:5px 0; max-width:70%; float:right; clear:both;">
                <b>You:</b> {msg['user']}<br>
                <small>{msg['time']}</small>
            </div>
            """
            # Bot message
            chat_html += f"""
            <div style="background-color:#E8E8E8; padding:10px; border-radius:10px; margin:5px 0; max-width:70%; float:left; clear:both;">
                <b>Bot:</b> {msg['bot']}<br>
                <small>{msg['time']}</small>
            </div>
            """
        chat_html += "</div>"
        chat_box.markdown(chat_html, unsafe_allow_html=True)

# ---------------- Styling ----------------
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    height: 3em;
    width: 100%;
    font-size:16px;
}
.stTextInput>div>div>input {
    font-size: 16px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

