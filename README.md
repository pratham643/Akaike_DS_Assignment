

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
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key  
1. Sign up at [NewsAPI](https://newsapi.org/) to get a free API key.  
2. Set the key in your environment:  
```bash
export NEWS_API_KEY=your_api_key
```

---

## 🖥️ Usage  

### Run the Streamlit App  
```bash
streamlit run app.py
```

### 💡 What happens?  
1. You enter a company name (e.g., Tesla, Google).  
2. The app fetches, summarizes, and analyzes the news.  
3. You see news cards with sentiment analysis.  
4. You hear a Hindi TTS summary.  

### Run API Server  
```bash
python api.py
```

#### API Endpoints  
- **GET** `/fetch-news?company=Tesla` → Fetch latest news.  
- **POST** `/analyze-sentiment` → Analyze sentiment of given text.  

