from flask import Flask, request, jsonify
from lyrics_api import get_lyrics
from analyze_api import analyze_sentiment
from recommend_api import recommend_tracks

app = Flask(__name__)

@app.route("/lyrics", methods=["GET"])
def lyrics():
    query = request.args.get("query")
    lyrics = get_lyrics(query)
    return jsonify({"lyrics": lyrics})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("lyrics", "")
    result = analyze_sentiment(text)
    return jsonify(result)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    sentiment = data.get("sentiment", "")
    tracks = recommend_tracks(sentiment)
    return jsonify({"tracks": tracks})

if __name__ == "__main__":
    app.run(debug=True)
