import streamlit as st
import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import os
from gtts import gTTS

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_newsapi_articles(company_name: str, num_results: int = 10):
    """Fetch articles using NewsAPI"""
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": company_name,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": num_results
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "articles" not in data:
            st.warning("No articles found.")
            return []
        return data["articles"]
    except requests.RequestException as e:
        st.error(f"Error fetching news: {e}")
        return []

def summarize_text(text):
    """Extract first two meaningful sentences"""
    sentences = [s.strip() for s in text.split(". ") if s.strip()]
    return ". ".join(sentences[:2]) + "." if len(sentences) > 1 else text

def analyze_sentiment_vader(text):
    """Perform sentiment analysis using VADER"""
    scores = sid.polarity_scores(text)
    compound = scores['compound']
    return "Positive" if compound > 0.1 else "Negative" if compound < -0.1 else "Neutral"

def generate_hindi_tts(text):
    """Generate Hindi TTS audio"""
    tts = gTTS(text, lang="hi")
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

def generate_report(company_name):
    """Generate structured report"""
    with st.spinner(f"Fetching news articles for {company_name}..."):
        articles_data = fetch_newsapi_articles(company_name, num_results=10)
        articles = []

        for article in articles_data:
            summary = summarize_text(article.get("description") or article.get("content") or "")
            sentiment = analyze_sentiment_vader(summary)
            articles.append({
                "Title": article["title"],
                "Summary": summary,
                "Sentiment": sentiment,
                "URL": article["url"]
            })

        if not articles:
            st.error("No valid articles found.")
            return

        sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
        for article in articles:
            sentiment_counts[article["Sentiment"]] += 1

        final_sentiment = f"कंपनी {company_name} की हाल की खबरों के अनुसार, सकारात्मक ({sentiment_counts['Positive']}), नकारात्मक ({sentiment_counts['Negative']}), और तटस्थ ({sentiment_counts['Neutral']}) समीक्षाएं मिलीं।"

        report = {
            "Company": company_name,
            "Articles": articles,
            "Sentiment Distribution": sentiment_counts,
            "Final Sentiment Analysis": final_sentiment,
            "Audio": "[Play Hindi Speech]"
        }

        audio_file = generate_hindi_tts(final_sentiment)
        st.json(report)
        st.audio(audio_file, format="audio/mp3")
