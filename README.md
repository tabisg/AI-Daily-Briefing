\\🤖 AI News Auditor & Podcast Ecosystem (RAG Pipeline)
📌 Overview
This project is an automated, end-to-end Retrieval-Augmented Generation (RAG) pipeline. It autonomously ingests global news and developer trends, audits them for sentiment and credibility (Truth-O-Meter), and utilizes Gemini 2.5 Flash to generate noise-free daily briefings and automated Audio Podcasts.

🏗️ Architecture & Tech Stack
Data Ingestion: Python (Real-time RSS Feeds & Verified Web Aggregation).

Vector Database: ChromaDB (Serves as the system's long-term contextual memory).

Orchestration: LangChain.

Generative AI (Brain): Google Gemini 2.5 Flash API.

Audio Engine: gTTS (Google Text-to-Speech).

Deployment: Streamlit Cloud for the application and Vercel DNS for custom domain management.

🚧 Engineering Challenges Overcome
The Data Reliability Pivot
During development, reliance on social media APIs (like X/Twitter) proved problematic due to extreme rate limits and a high noise-to-signal ratio. To ensure production-grade reliability, I engineered a transition to a custom RSS and Verified Web Aggregator pipeline. This shift provided structured, high-quality data, significantly improving the accuracy of the "Truth-O-Meter" and sentiment analysis. The system is live-hosted on a custom subdomain at news.tabish.tech for seamless accessibility.

⚙️ How It Works
Data Extraction: run_pipeline.py fetches the latest developer updates (Python, React, AI trends) and verified entertainment news from global authoritative sources.

Vectorization & Auditing: Raw text is embedded into ChromaDB for semantic search capabilities. Gemini 2.5 Flash then audits each article to calculate sentiment and a credibility score.

Synthesis: The system converts the generated summaries into voice briefings using a Text-to-Speech engine, allowing users to consume news as a morning podcast.

Automation & Live Hosting: The entire pipeline is scheduled and live-hosted. Users can access insights and audio files directly through an interactive dashboard.
