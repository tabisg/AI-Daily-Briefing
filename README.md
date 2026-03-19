# 🤖 AI News Auditor & Podcast Ecosystem (RAG Pipeline)

[![Live App](https://img.shields.io/badge/Live-news.tabish.tech-blue?style=for-the-badge&logo=vercel)](http://news.tabish.tech)
[![Portfolio](https://img.shields.io/badge/Portfolio-tabish.tech-black?style=for-the-badge&logo=django)](https://tabish.tech)

## 📌 Overview
This project is an automated, end-to-end **Retrieval-Augmented Generation (RAG)** pipeline. It autonomously ingests global news and developer trends, audits them for sentiment and credibility (Truth-O-Meter), and utilizes **Gemini 2.5 Flash** to generate noise-free daily briefings and automated **Audio Podcasts**.

## 🏗️ Architecture & Tech Stack
* **Data Ingestion:** Python (Real-time RSS Feeds & Verified Web Aggregation).
* **Vector Database:** ChromaDB (Long-term Contextual Memory).
* **Orchestration:** LangChain.
* **Generative AI:** Google Gemini 2.5 Flash API.
* **Audio Engine:** gTTS (Google Text-to-Speech).
* **Deployment:** Streamlit Cloud & Vercel DNS.



## 🚧 Engineering Challenges Overcome
**The Data Reliability Pivot:**
During development, reliance on social media APIs (like X/Twitter) proved problematic due to extreme rate limits and data noise. I engineered a transition to a custom **RSS and Verified Web Aggregator pipeline**, which significantly improved the accuracy of the "Truth-O-Meter" and sentiment analysis by focusing on authoritative sources.

## ⚙️ How It Works
1. **Data Extraction:** `run_pipeline.py` fetches updates from global authoritative sources.
2. **Vectorization & Auditing:** Raw text is embedded into ChromaDB. Gemini 2.5 Flash audits each article for sentiment and credibility scores.
3. **Synthesis:** System converts summaries into voice briefings using a Text-to-Speech engine.
4. **Automation:** The entire pipeline is scheduled and live-hosted at `news.tabish.tech`.

## 🚀 How to Run Locally

### 1. Prerequisites
* **Python 3.12+** installed.
* **Gemini API Key** from Google AI Studio.

### 2. Installation
```bash
# Clone the repo
git clone [https://github.com/tabisg/ai-news-auditor.git](https://github.com/tabisg/ai-news-auditor.git)
cd ai-news-auditor

# Install dependencies
python -m pip install -r requirements.txt
