---
title: News Insight
emoji: 📰
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.43.2
app_file: app.py
pinned: false
---

# 📢 News Insight – Simplified News Summarizer with Sentiment Analysis  

🚀 **News Insight** is a minimalistic web app that fetches real-time news, summarizes articles, analyzes sentiment, and generates a **Hindi text-to-speech (TTS)** summary.  

Built with ❤️ by **Prathmesh**  

---

## 📌 Features  

✅ Fetches **real-time news** from multiple sources.  
✅ **Summarizes** news articles for quick insights.  
✅ Performs **sentiment analysis** (Positive, Negative, Neutral).  
✅ Generates **Hindi text-to-speech (TTS)** for easy listening.  
✅ **Card-based UI** – Simple, lightweight, and distraction-free.  

---

## 🛠️ Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-repo/news-insight.git
cd news-insight

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up API Key

1.Sign up at NewsAPI to get a free API key.
2.Set the key in your environment.

export NEWS_API_KEY=your_api_key

🖥️ Usage
🔹 Run the Streamlit App

streamlit run app.py

💡 What happens?

🔹You enter a company name (e.g., Tesla, Google).
🔹🔹The app fetches, summarizes, and analyzes the news.
🔹🔹🔹You see news cards with sentiment analysis.
🔹🔹🔹🔹You hear a Hindi TTS summary.

🔹🔹 Run API Server

python api.py

🔹GET /fetch-news?company=Tesla → Fetch latest news.
🔹🔹POST /analyze-sentiment → Analyze sentiment of given text.