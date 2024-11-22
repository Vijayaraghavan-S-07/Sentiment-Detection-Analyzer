from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# def index():
def sentimentanalysis(text):
    # if request.method == "POST":
        # Get user input from the form
        # user_input = request.form["text"]
        
        # Perform sentiment analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity
    # polarity = blob.sentiment.polarity  # Polarity score (-1.0 to 1.0)
    # subjectivity = blob.sentiment.subjectivity  # Subjectivity score (0.0 to 1.0)
    
    # Classify sentiment
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    # Render the results on the same page
    # return render_template(
    #     "index.html", 
    #     sentiment=sentiment, 
    #     polarity=round(polarity, 2), 
    #     subjectivity=round(subjectivity, 2), 
    #     user_input=user_input
    # )
    
    return sentiment
    
    # Default GET request
    # return render_template("index.html", sentiment=None)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    
    if request.method == "POST":
        text = request.form["text"]
        sentiment = sentimentanalysis(text)
    
    return render_template("index.html", sentiment=sentiment)    
    
if __name__ == "__main__":
    app.run(debug=True)
