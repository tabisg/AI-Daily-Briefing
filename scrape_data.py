import random
import time

def fetch_unofficial_tweets():
    print("🚀 Simulating connection to real-time data feed...\n")
    time.sleep(1.5) # Pauses briefly to simulate network latency

    # Our local dataset of developer and entertainment trends
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

    try:
        print("💻 Extracting Developer (Tech) trends...")
        time.sleep(1)
        # Randomly grab 3 tech tweets to simulate a live changing feed
        dev_tweets = random.sample(mock_database["dev"], 3)
        for tweet in dev_tweets:
            print(f"[DEV]: {tweet}\n")
            time.sleep(0.5)
            
        print("🎬 Extracting Entertainment trends...")
        time.sleep(1)
        # Randomly grab 3 entertainment tweets
        ent_tweets = random.sample(mock_database["ent"], 3)
        for tweet in ent_tweets:
            print(f"[ENT]: {tweet}\n")
            time.sleep(0.5)

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    fetch_unofficial_tweets()