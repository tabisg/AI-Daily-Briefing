import os
import concurrent.futures
import feedparser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# MAGIC KEY for Streamlit Secrets (if available)
try:
    import streamlit as st
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
except:
    pass



def fetch_single_category(category, url):
    """Ek single category laane ka fast function"""
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:6]:
         items.append(f"Category: {category}\nTitle: {entry.title}\nSummary: {entry.summary}")
    return items

def fetch_trending_news():
    urls = {
        "Technology": "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=en-IN&gl=IN&ceid=IN:en",
        "Sports": "https://news.google.com/rss/headlines/section/topic/SPORTS?hl=en-IN&gl=IN&ceid=IN:en",
        "Business": "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=en-IN&gl=IN&ceid=IN:en",
        "Entertainment": "https://news.google.com/rss/headlines/section/topic/ENTERTAINMENT?hl=en-IN&gl=IN&ceid=IN:en",
        "World": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=en-IN&gl=IN&ceid=IN:en"
    }
    
    all_news = []
    
    # 🚀 The Multi-Threading Magic: 5 URLs ek saath fetch honge!
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 5 parallel tasks start kardiye
        futures = [executor.submit(fetch_single_category, cat, url) for cat, url in urls.items()]
        
        # Jaise jaise data aata jayega, list mein add hota jayega
        for future in concurrent.futures.as_completed(futures):
            all_news.extend(future.result())
            
    return "\n\n".join(all_news)

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