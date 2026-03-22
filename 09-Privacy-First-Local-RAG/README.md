# Project 09: Private "Privacy-First" Legal/Medical Assistant

## Overview
A fully offline AI assistant for sensitive industries where data privacy is non-negotiable. No data ever leaves the local hardware.

## Key Features
- **Local Inference**: Uses **Ollama** or **vLLM** for local model execution.
- **Local Embeddings**: Runs embedding models (like Nomic or BGE) locally.
- **Persistent Local DB**: Chroma or Qdrant running in a Docker container or local folder.

## Tech Stack
- **Core Runtime**: Ollama
- **Model**: Llama 3.1 8B / Mistral Nemo
- **Vector DB**: ChromaDB
- **UI**: Private desktop app (Streamlit / Electron)

## Target Audience
- **Legal Professionals**: Analyzing case files.
- **Healthcare**: Privacy-compliant patient record analysis.
- **Financial Services**: Internal document search.
