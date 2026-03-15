import os
import feedparser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# MAGIC KEY for Streamlit Secrets (if available)
try:
    import streamlit as st
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
except:
    pass

def fetch_trending_news():
    # 🚀 Naya Upgrade: now we fetch new data for every categeory 
    urls = {
        "Technology": "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=en-IN&gl=IN&ceid=IN:en",
        "Sports": "https://news.google.com/rss/headlines/section/topic/SPORTS?hl=en-IN&gl=IN&ceid=IN:en",
        "Business": "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=en-IN&gl=IN&ceid=IN:en",
        "Entertainment": "https://news.google.com/rss/headlines/section/topic/ENTERTAINMENT?hl=en-IN&gl=IN&ceid=IN:en",
        "World": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=en-IN&gl=IN&ceid=IN:en"
    }
    
    news_items = []
    
    # everynews category ke liye top 6 articles fetch karenge
    for category, url in urls.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:6]:
            news_items.append(f"Category: {category}\nTitle: {entry.title}\nSummary: {entry.summary}")
            
    return "\n\n".join(news_items)

def generate_newsletter():
    # New Upgrade: Ab hum har category ke liye alag se data fetch karenge, taaki Gemini ko zyada fresh aur relevant news mile.
    trending_data = fetch_trending_news()
    
    llm = ChatGoogleGenerativeAI(
        api_key=os.environ.get("GEMINI_API_KEY"),
        model="gemini-2.5-flash",  # <--- Welcome to 2026! Yeh Google ka sabse naya aur active model hai
        temperature=0.3
    )
    
   # 🚀 THE STRICT GROUPED INSHORTS PROMPT
    template = """
    You are an expert News Editor creating an 'Inshorts' style daily feed.
    Below are the top trending news articles of the day, fetched by category.

    Your task is to GROUP the news by their Category. 
    Print the Category Header ONLY ONCE, and then list all the news articles for that category below it.

    You MUST format it EXACTLY in this Markdown structure. Keep the exact blank lines:

    ## [Category Emoji] [Category Name]

    **[Catchy, Bold Headline 1]**
    
    [A crisp, engaging summary in EXACTLY 60 words.]
    
    ---
    
    **[Catchy, Bold Headline 2]**
    
    [A crisp, engaging summary in EXACTLY 60 words.]
    
    ---

    Do NOT write any intro or outro text (like 'Here is the news'). 
    Do NOT repeat the category header for every single news item.

    Raw News Data:
    {context}
    """
    
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    
    response = chain.invoke({"context": trending_data})
    return response.content

if __name__ == "__main__":
    print(generate_newsletter())