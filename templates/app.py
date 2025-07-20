import json
import random
from flask import Flask, render_template, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# --- Boilerplate and Setup ---
# Initialize the Flask app
app = Flask(__name__)

# Download the VADER lexicon for sentiment analysis (only needs to be done once)
# This is a simple but effective NLP model included with the NLTK library.
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    print("Downloading VADER lexicon...")
    nltk.downloader.download('vader_lexicon')

# --- Simulated Data ---
# In a real-world system, this data would come from a live Twitter stream via Kafka.
# To make this project easy to run, we simulate the tweets here.
SIMULATED_TWEETS = [
    "Just tried the new Google Pixel, the camera is absolutely mind-blowing! #google",
    "The new AI features in Android are a game-changer. So intuitive!",
    "I'm so excited for the new developments in machine learning this year.",
    "Spent the whole day debugging a C++ memory leak... the struggle is real.",
    "The performance of this new JavaScript framework is incredible.",
    "I wish this API had better documentation, it's so frustrating to use.",
    "Just deployed my first app on Google Cloud Platform. It was surprisingly easy!",
    "The scalability of distributed systems is a fascinating and complex topic.",
    "Horrible customer service experience today. So disappointed.",
    "Attending a tech talk on natural language processing, this is the future!",
    "My code finally compiled without any errors. What a great feeling!",
    "This app keeps crashing, it's completely unusable.",
]

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# --- API Endpoints ---
# This is the main route that serves the HTML page.
@app.route('/')
def index():
    """Renders the main dashboard page."""
    return render_template('index.html')

# This is the API endpoint that the frontend will call to get sentiment data.
@app.route('/data')
def get_data():
    """
    Analyzes a random tweet and returns the tweet and its sentiment score.
    This simulates a real-time data feed.
    """
    # Pick a random tweet from our simulated list
    tweet = random.choice(SIMULATED_TWEETS)
    
    # Calculate sentiment scores using the VADER model
    # The 'compound' score is a single value from -1 (most negative) to 1 (most positive).
    sentiment_scores = sid.polarity_scores(tweet)
    compound_score = sentiment_scores['compound']
    
    # Categorize the sentiment based on the compound score
    if compound_score >= 0.05:
        sentiment_label = 'Positive'
    elif compound_score <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'
        
    # Prepare the data to be sent to the frontend as JSON
    data = {
        'tweet': tweet,
        'sentiment_label': sentiment_label,
        'score': compound_score,
        'timestamp': json.dumps(random.randint(1, 1000)) # simulate a timestamp
    }
    
    return jsonify(data)

# --- Main Execution ---
if __name__ == '__main__':
    # Runs the Flask app. The host '0.0.0.0' makes it accessible on your local network.
    app.run(host='0.0.0.0', port=8080, debug=True)
