import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI

st.set_page_config(page_title="GenAI News Insights", layout="wide")

def get_news(url):
    # Mock scraper logic
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [h.text for h in soup.find_all('h2')[:10]]
    return headlines

def summarize_headlines(headlines):
    llm = ChatOpenAI(model="gpt-4o-mini")
    prompt = f"Summarize these news headlines into 3 key bullet points:\n" + "\n".join(headlines)
    return llm.invoke(prompt).content

st.title("🗞️ Automated News Insights Dashboard")

url = st.text_input("Enter News URL", "https://techcrunch.com/")

if st.button("Scrape & Summarize"):
    with st.spinner("Fetching news..."):
        try:
            headlines = get_news(url)
            st.subheader("Latest Headlines")
            for h in headlines:
                st.write(f"- {h}")
            
            summary = summarize_headlines(headlines)
            st.subheader("AI Summary")
            st.info(summary)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    # Run with: streamlit run news_dashboard.py
    pass
