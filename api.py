from flask import Flask, request, jsonify
from utils import fetch_newsapi_articles, analyze_sentiment_vader, summarize_text

app = Flask(__name__)

@app.route("/fetch-news", methods=["GET"])
def fetch_news():
    company_name = request.args.get("company")
    if not company_name:
        return jsonify({"error": "Company name is required"}), 400
    
    articles = fetch_newsapi_articles(company_name)
    return jsonify(articles)

@app.route("/analyze-sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.json
    if "text" not in data:
        return jsonify({"error": "Text is required"}), 400
    
    sentiment = analyze_sentiment_vader(data["text"])
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
