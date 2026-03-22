# Project 06: SQL-Agent with Auto-Visualization

## Overview
A business intelligence agent that takes Natural Language (NL) questions, converts them to complex SQL queries, executes them against a database, and automatically selects the best chart for visualization.

## Key Features
- **NL-to-SQL**: Understands nested joins, aggregations, and filtering in plain English.
- **Auto-Charting**: Intelligently chooses between Bar, Line, Pie, or Scatter plots based on the data structure.
- **Dynamic Feedback**: Explains the SQL query to the user for transparency.

## Tech Stack
- **Database**: PostgreSQL / MySQL / SQLite
- **LLM**: GPT-4o / Claude 3.5 Sonnet
- **Visualization**: Plotly / Matplotlib / Streamlit
- **Framework**: LangChain SQL Agent

## Sample Workflow
- **User**: "Show me the trend of sales for 'Category A' over the last 6 months."
- **Agent**: Generates SQL -> Executes -> Sees time-series data -> Renders Line Chart using Plotly.
