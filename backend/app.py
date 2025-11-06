from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# backend から1階層上の .env を明示的に読み込む
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# APIキーを確認（初期テスト用）
print("Spotify Client ID:", os.getenv("SPOTIFY_CLIENT_ID"))
print("Genius Token (前半10文字):", os.getenv("GENIUS_ACCESS_TOKEN")[:10] + "...")

# ===== Flaskアプリ設定 =====
app = Flask(__name__)

# ===== 各APIルート =====
@app.route("/lyrics", methods=["GET"])
def lyrics():
    query = request.args.get("query")
    from lyrics_api import get_lyrics
    lyrics = get_lyrics(query)
    return jsonify({"lyrics": lyrics})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("lyrics", "")
    from analyze_api import analyze_sentiment
    result = analyze_sentiment(text)
    return jsonify(result)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    sentiment = data.get("sentiment", "")
    from recommend_api import recommend_tracks
    tracks = recommend_tracks(sentiment)
    return jsonify({"tracks": tracks})

if __name__ == "__main__":
    app.run(debug=True)