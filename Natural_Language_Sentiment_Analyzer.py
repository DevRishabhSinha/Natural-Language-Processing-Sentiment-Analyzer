from textblob import TextBlob


# Define a function to detect sentiment
def detect_sentiment(text):
    # Create a TextBlob object with the given text
    blob = TextBlob(text)

    # Get the polarity score of the text
    # The polarity score is a float between -1 and 1, where negative values indicate negative sentiment,
    # positive values indicate positive sentiment, and 0 indicates neutral sentiment
    sentiment_score = blob.sentiment.polarity

    # Determine the sentiment based on the polarity score
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Return the sentiment and polarity score as a tuple
    return sentiment, sentiment_score


# Example usage:
text = "I love spending time with my family!"
sentiment, score = detect_sentiment(text)
print(f"The sentiment of '{text}' is {sentiment} with a score of {score:.2f}")
