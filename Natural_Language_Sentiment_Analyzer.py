import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Define a function to scrape text from a web page
def scrape_text(url):
    # Make a GET request to the URL and get the response content
    response = requests.get(url)
    content = response.content
    
    # Use BeautifulSoup to parse the HTML content and extract the text
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    
    # Remove any leading/trailing whitespace and newlines
    text = text.strip().replace('\n', '')
    
    # Return the scraped text
    return text

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

# Define the URL of the web page to scrape
url = "https://www.bloomberg.com/"

# Scrape the text from the web page
text = scrape_text(url)

# Detect the sentiment of the scraped text
sentiment, score = detect_sentiment(text)

# Print the results
print(f"The sentiment of the text from {url} is {sentiment} with a score of {score:.2f}")
