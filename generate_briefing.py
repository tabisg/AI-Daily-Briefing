import os
import feedparser
import concurrent.futures
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Model Setup (2026 Latest)
llm = ChatGoogleGenerativeAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    model="gemini-2.5-flash", 
    temperature=0.3
)

def fetch_single_category(category, url):
    feed = feedparser.parse(url)
    items = []
    # only take top 3 news from each category to keep it concise for the AI
    for entry in feed.entries[:3]:
        items.append(f"Category: {category} | Title: {entry.title}")
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
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_single_category, cat, url) for cat, url in urls.items()]
        for future in concurrent.futures.as_completed(futures):
            all_news.extend(future.result())
    return "\n".join(all_news)

def generate_newsletter():
    trending_data = fetch_trending_news()


 # ✨ THE ULTIMATE AESTHETIC AUDITOR PROMPT
    template = """
    You are a high-end Digital Editor and Fact-Checker. Create a 'Daily Buzz' feed that is beautiful, fast, and insightful.
    
    INSTRUCTIONS:
    1. Group news by category with a BIG header and a relevant emoji (## [Emoji] [Category]).
    2. For each news, write a very catchy bold title.
    3. Right below the title, add a 'Quick Scan' line: [Sentiment Emoji] Mood: [Sentiment] | [Trust Emoji] Trust Score: [0-100]%
    4. Below that, write ONLY 2 bullet points (max 15 words each).
    5. Start each bullet with a unique, relevant emoji.
    6. Ensure a clean visual hierarchy with "---" between news items.

    FORMAT EXAMPLE:
    ## 🚀 Technology
    **Apple Reveals New AI Chip**
    > 🟢 Mood: Positive | ✅ Trust Score: 98%
    - ⚡ 50% faster than previous models.
    - 🔋 Saves 40% more battery life.
    ---

    RAW NEWS:
    {context}
    """

    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    response = chain.invoke({"context": trending_data})
    return response.content

if __name__ == "__main__":
    print(generate_newsletter())