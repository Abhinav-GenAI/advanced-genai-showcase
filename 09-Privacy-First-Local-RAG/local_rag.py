import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA

def run_local_rag(file_path, query):
    # 1. Local Embeddings (Ollama)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    # 2. Load & Split
    loader = TextLoader(file_path)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(data)
    
    # 3. Local Vector Store (Chroma)
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory="./local_chroma")
    
    # 4. Local LLM (Ollama)
    llm = Ollama(model="llama3")
    
    # 5. Chain
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())
    
    # 6. Query
    # return qa.invoke(query)
    print("Local-only RAG pipeline initialized. No data leaves the machine.")

if __name__ == "__main__":
    # run_local_rag("sensitive_data.txt", "What are the key terms?")
    print("Privacy-First Local RAG script ready. Ensure Ollama is running.")
