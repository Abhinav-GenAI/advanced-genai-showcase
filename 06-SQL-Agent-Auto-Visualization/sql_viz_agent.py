import os
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
import plotly.express as px
import pandas as pd

def run_sql_query_and_viz(db_uri, query_text):
    # 1. Connect to DB
    db = SQLDatabase.from_uri(db_uri)
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # 2. Initialize SQL Agent
    agent_executor = create_sql_agent(llm, db=db, verbose=True)

    # 3. Run Query
    # result = agent_executor.invoke(query_text)
    
    # 4. Mock Visualization Logic
    # In a real app, you'd extract the tabular result and call Plotly
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr"],
        "Sales": [100, 150, 130, 200]
    }
    df = pd.DataFrame(data)
    fig = px.line(df, x="Month", y="Sales", title="Automated Sales Trend Chart")
    # fig.show()
    print("SQL Agent with Auto-Viz initialized.")

if __name__ == "__main__":
    # run_sql_query_and_viz("sqlite:///sample.db", "How many users joined in the last 30 days?")
    print("Script ready. Connect to a valid DB URI to execute queries.")
