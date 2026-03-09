import chromadb

def setup_database():
    print("🧠 Setting up the AI Memory (Vector DB)...")
    
    # 1. Create a local database folder named "chroma_db" on your computer
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # 2. Create a "collection" (Think of this like a folder for your data)
    # ChromaDB will automatically download a free, open-source AI embedding model to process the text!
    collection = client.get_or_create_collection(name="trend_chatter")
    
    # 3. Test data: Developer and Entertainment trends
    sample_tweets = [
        "React 19 is finally out! The new compiler is incredibly fast.",
        "Just saw the new Marvel movie trailer. The CGI looks completely different!",
        "Python 3.12 makes f-strings so much easier to use for data engineering.",
        "Box office numbers for the weekend are breaking all previous records."
    ]
    
    # Each piece of data needs a unique ID and a category tag
    ids = ["tweet_1", "tweet_2", "tweet_3", "tweet_4"]
    metadatas = [{"category": "dev"}, {"category": "ent"}, {"category": "dev"}, {"category": "ent"}]
    
    # 4. Convert to math and save to the database!
    collection.add(
        documents=sample_tweets,
        metadatas=metadatas,
        ids=ids
    )
    
    print("✅ Data successfully converted to vectors and saved!")
    print(f"📊 Total items stored in memory: {collection.count()}")

if __name__ == "__main__":
    setup_database()