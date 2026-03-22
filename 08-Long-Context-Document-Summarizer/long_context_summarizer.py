import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.docstore.document import Document

load_dotenv()

def summarize_long_docs(file_paths):
    # 1. Initialize Gemini 1.5 Pro (Massive 1M+ Context)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    # 2. Combine all content into one context
    full_text = ""
    for path in file_paths:
        with open(path, "r", encoding="utf-8") as f:
            full_text += f"\n--- Start of {os.path.basename(path)} ---\n"
            full_text += f.read()
    
    # 3. Massive Context Prompt
    prompt = f"Summarize the main themes and specific cross-document connections from the following text:\n\n{full_text}"
    
    # 4. Invoke
    # response = llm.invoke(prompt)
    # return response.content
    print(f"Loaded {len(full_text)} characters for analysis. High-context prompt ready.")

if __name__ == "__main__":
    # summarize_long_docs(["file1.txt", "file2.txt"])
    print("Long-Context Summarizer script ready. Best used with Gemini 1.5 Pro.")
