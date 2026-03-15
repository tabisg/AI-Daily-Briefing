import os
import feedparser
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

#  For Streamlit Cloud magic trick to access secrets in this standalone script
try:
    import streamlit as st
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except:
    pass

def fetch_trending_news():
    # Google News (Global + India Trending)
    url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(url)
    
    news_items = []
    # FIX: now we are taking only top 6 news items to keep it concise for the LLM
    for entry in feed.entries[:6]:
        # FIX: summary are usually long, we will truncate it to 300 characters for the LLM to process better
        short_summary = entry.summary[:300] + "..." 
        news_items.append(f"Title: {entry.title}\nSummary: {short_summary}")
        
    return "\n\n".join(news_items)
def generate_newsletter():
    print("🌍 Fetching Global Trending News...")
    trending_data = fetch_trending_news()
    
    print("🧠 Processing with Llama-3 (Inshorts Style)...")
    llm = ChatGroq(
        api_key=os.environ.get("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0.3
    )
    
    # THE INSHORTS PROMPT
    template = """
    You are an expert News Editor creating an 'Inshorts' style daily feed.
    Below are the top trending news articles of the day from various fields (Politics, Sports, Business, Technology, Entertainment, etc.).

    For each news item, provide:
    1. An appropriate Category Emoji and Name (e.g., 🏏 Sports, 💰 Business, 🌍 World News)
    2. A catchy, bold Headline
    3. A crisp, engaging summary in EXACTLY 60 words.

    Format them clearly as separate news cards with a horizontal line (---) between them. Do not include any intro or outro text.

    Raw News Data:
    {context}
    """
    
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    
    response = chain.invoke({"context": trending_data})
    return response.content

if __name__ == "__main__":
    print(generate_newsletter())