def recommend_tracks(sentiment):
    # デモ用：最初は固定リスト
    if sentiment == "positive":
        return ["Happy - Pharrell", "Good Day - Nappy Roots"]
    elif sentiment == "negative":
        return ["Someone Like You - Adele", "Fix You - Coldplay"]
    else:
        return ["Let It Be - The Beatles", "Imagine - John Lennon"]
