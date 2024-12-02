from textblob import TextBlob # type: ignore

def analyze_sentiment(text):
    """Analyze the sentiment of the given text."""
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Range: -1 (negative) to 1 (positive)

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Test the function
if __name__ == "__main__":
    sample_text = "I love programming in Python!"
    result = analyze_sentiment(sample_text)
    print(f"Sentiment: {result}")