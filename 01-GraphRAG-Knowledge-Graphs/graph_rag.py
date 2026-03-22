import networkx as nx
import matplotlib.pyplot as plt
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List

# 1. Define Data Structure for Triplets
class Triplet(BaseModel):
    subject: str = Field(description="The source entity")
    predicate: str = Field(description="The relationship between subject and object")
    obj: str = Field(description="The target entity")

class Triplets(BaseModel):
    triplets: List[Triplet]

# 2. Extract Triples using LLM
def extract_triplets(text: str):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    parser = JsonOutputParser(pydantic_object=Triplets)
    
    prompt = PromptTemplate(
        template="Extract entities and their relationships from the following text as a list of triplets.\n{format_instructions}\nText: {text}",
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    
    chain = prompt | llm | parser
    return chain.invoke({"text": text})

# 3. Build and Visualize Graph
def build_graph(triplets_data):
    G = nx.DiGraph()
    for triplet in triplets_data["triplets"]:
        G.add_edge(triplet["subject"], triplet["obj"], label=triplet["predicate"])
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Knowledge Graph Extracted from Text")
    # plt.show() # Uncomment to see the graph
    print("Graph built with nodes:", G.nodes())

if __name__ == "__main__":
    sample_text = "Elon Musk founded SpaceX in 2002. SpaceX is headquartered in California."
    # triplets = extract_triplets(sample_text)
    # build_graph(triplets)
    print("GraphRAG Script ready. Ensure OPENAI_API_KEY is set to run extraction.")
