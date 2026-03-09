import chromadb

# 1. Connect to your local database folder
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="trend_chatter")

# 2. Ask the database to find semantically similar tweets
search_results = collection.query(
    query_texts=["Tell me about new coding tools or programming languages"], # You can also search for movies or box office news here
    n_results=2 # Limit the output to the top 2 most relevant results
)

# 3. Print the results to the terminal
print("🔍 Your Search Results:\n")
for result in search_results['documents'][0]:
    print(f"- {result}")