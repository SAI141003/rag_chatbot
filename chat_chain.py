from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

def create_qa_chain(vector_store):
    # Setup retriever from vector store
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # Load FLAN-T5-Small model
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Create a HuggingFace pipeline
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    llm = HuggingFacePipeline(pipeline=pipe)

    # Create the RAG QA chain
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
