# Project 01: GraphRAG Implementation (Knowledge Graphs)

## Overview
Standard RAG often misses global relationships. **GraphRAG** combines Knowledge Graphs (KG) with Vector Search to enable "multi-hop" reasoning and a holistic understanding of complex datasets.

## Key Features
- **Knowledge Extraction**: Uses LLMs to identify entities and relationships from unstructured text.
- **Graph Storage**: Stores data in **Neo4j** or **NetworkX**.
- **Hybrid Retrieval**: Combines vector similarity with graph traversal to find deep context.

## Tech Stack
- **Graph Database**: Neo4j / NetworkX
- **Orchestration**: LangChain / LlamaIndex
- **LLM**: GPT-4o / Claude 3.5 Sonnet
- **Embeddings**: OpenAI / HuggingFace

## Architecture
1. **Ingest**: Extract (Entity, Relationship, Entity) triplets.
2. **Index**: Store triplets in a Graph DB and summaries in a Vector DB.
3. **Query**: Traversing the graph from specific entities to find related clusters.
4. **Answer**: Synthesizing the graph context for a high-level response.
