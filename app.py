import streamlit as st
from agents.scraper_agent import ScraperAgent
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
agent = ScraperAgent(api_key)

st.title("📰 News Scraper Agent")

query = st.text_input("Enter topic:", "Mumbai")

if st.button("Fetch News"):
    articles = agent.fetch_news(query)

    for art in articles:
        st.subheader(art["title"])
        st.write("Source:", art["source"]["name"])

        if st.button(f"Get Full Article: {art['title'][:20]}"):
            content = agent.get_full_article(art["url"])
            st.text_area("Content", content, height=200)

        st.divider()