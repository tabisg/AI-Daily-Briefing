import chromadb
import random
import time
import uuid

def run_data_pipeline():
    print("⚙️ Starting the Automated Data Pipeline...\n")
    
    # 1. Connect to our existing AI Memory (ChromaDB)
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="trend_chatter")
    
    # 2. Our simulated live feed (The "Internet")
    mock_database = {
        "dev": [
            "Python 3.12 is lightning fast! The new error messages are a lifesaver.",
            "Just deployed my first agent using LangChain and React. Mind blown.",
            "AI is moving too fast. How is everyone keeping up with these new LLMs?",
            "Stop using standard databases for AI. Vector DBs like Chroma are the future.",
            "The new API rate limits are forcing developers to get creative with web scraping."
        ],
        "ent": [
            "The new Marvel trailer just broke the internet. CGI looks completely different!",
            "Box office numbers for the weekend are out. Cinema is officially back.",
            "GTA 6 rumors are going crazy today. The map looks massive.",
            "Who else is binge-watching the new sci-fi series tonight?",
            "Can't believe the plot twist in that finale. Best writing in television right now."
        ]
    }
    
    print("📡 Extracting live trends...")
    time.sleep(1)
    
    # Grab 3 random tweets from each category
    dev_tweets = random.sample(mock_database["dev"], 3)
    ent_tweets = random.sample(mock_database["ent"], 3)
    
    # Combine the data for the database
    all_tweets = dev_tweets + ent_tweets
    metadatas = [{"category": "dev"}] * 3 + [{"category": "ent"}] * 3
    
    # Generate a unique mathematical ID for every single tweet using 'uuid'
    ids = [str(uuid.uuid4()) for _ in range(6)] 
    
    print(f"📥 Found {len(all_tweets)} new trends. Converting to vectors and saving to AI Memory...")
    
    # 3. Save to ChromaDB
    collection.add(
        documents=all_tweets,
        metadatas=metadatas,
        ids=ids
    )
    
    print("\n✅ Pipeline Complete! Data is safely stored.")
    print(f"📊 Total items now in memory: {collection.count()}")

if __name__ == "__main__":
    run_data_pipeline()