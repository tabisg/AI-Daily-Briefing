import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Block ChromaDB Telemetry BEFORE it imports so it doesn't freeze!
os.environ["ANONYMIZED_TELEMETRY"] = "False"

import chromadb
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

def generate_newsletter():
    print(" Waking up the AI Brain (Llama-3 via Groq)...")

   # 2. Connect to the LLM (Keep your real gsk_ key here!)
    llm = ChatGroq(
        api_key="YOUR_GROQ_API_KEY_HERE",  # <--- UPDATE THIS LINE
        model="llama-3.1-8b-instant",  # <--- UPDATE THIS LINE
        temperature=0.3 
    )

    # 3. Connect to your AI Memory (ChromaDB)
    print("🔍 Searching memory for today's trends...")
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="trend_chatter")

    # Pull all the saved tweets out of the database
    results = collection.get(include=["documents"])
    saved_tweets = results['documents']
    
    # Combine them into one big text block for the AI to read
    context_text = "\n".join(saved_tweets)

    # 4. Give the AI its instructions (Prompt Engineering)
    print(" Writing the daily briefing...\n")
    
    prompt_template = """
    You are an expert technology and entertainment journalist. 
    Read the following recent internet chatter and write a clean, professional daily briefing.
    
    Rules:
    1. Separate the briefing into two distinct sections: "💻 Developer Updates" and "🎬 Entertainment News".
    2. Use bullet points for readability.
    3. Keep it concise and punchy.
    4. Do NOT make up any information. ONLY use the provided context below.

    Context (Recent Internet Chatter):
    {context}

    Your Daily Briefing:
    """
    
    prompt = PromptTemplate.from_template(prompt_template)
    
    # 5. Connect the prompt and the LLM, then run it!
    chain = prompt | llm
    response = chain.invoke({"context": context_text})
    
    # 6. Print the final product
    print("==================================================")
    print(" YOUR AUTONOMOUS DAILY BRIEFING")
    print("==================================================\n")
    print(response.content)

if __name__ == "__main__":

    generate_newsletter()

