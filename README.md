# 🤖 Autonomous AI Curation Agent (RAG Pipeline)

## 📌 Overview
This project is an automated, end-to-end Retrieval-Augmented Generation (RAG) pipeline. It autonomously ingests daily internet chatter focusing on developer trends and entertainment news, embeds the text into a vector database, and utilizes a Large Language Model (LLM) to generate a formatted, noise-free daily briefing.

## 🏗️ Architecture & Tech Stack
* **Data Ingestion:** Python (Simulated Web/Social Scraping)
* **Vector Database (Memory):** ChromaDB 
* **Orchestration:** LangChain
* **Generative AI (Brain):** Meta Llama 3.1 (via Groq API)
* **Automation:** Windows Task Scheduler & Batch Scripting

## 🚧 Engineering Challenges Overcome
**The API Rate Limit Roadblock:**
During development, the official X (Twitter) Free Tier API heavily restricted read access. Instead of abandoning the project, I engineered a highly resilient "Mock-Live" simulated data ingestion feed. This allowed the vector database and LLM architecture to be fully tested and deployed without relying on expensive, rate-limited third-party APIs. 

## ⚙️ How It Works
1. **Data Extraction:** `run_pipeline.py` extracts the latest developer updates (Python, React, API trends) and entertainment news (box office, gaming).
2. **Vectorization:** The raw text is embedded into ChromaDB for semantic search capabilities.
3. **Generation:** `generate_briefing.py` retrieves the exact context from the database and passes it to Llama 3.1 with strict formatting instructions.
4. **Automation:** A local `run_agent.bat` script is scheduled via Windows Task Scheduler to trigger the pipeline daily, outputting a clean `latest_briefing.txt` file for morning reading.

## 🚀 How to Run Locally
1. Clone the repository.
2. Install requirements: `pip install langchain langchain-groq chromadb`
3. Add your own Groq API key to `generate_briefing.py`.
4. Run `run_pipeline.py` followed by `generate_briefing.py`.
