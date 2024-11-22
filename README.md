# Sentiment-Detection-Analyzer

# Web Application

This project is a simple web-based sentiment analysis tool. Users can input text into the application, and it will analyze the sentiment of the text, providing details such as polarity, subjectivity, and overall sentiment classification.

## Features
- **User Input Form**: Enter text for analysis through a simple text area form.
- **Sentiment Analysis**: Automatically classifies input text as positive, negative, or neutral.
- **Detailed Metrics**:
  - **Polarity**: Indicates the positivity or negativity of the text (-1 to 1).
  - **Subjectivity**: Measures how subjective or objective the text is (0 to 1).

## Technologies Used
- **Frontend**: HTML, Jinja2 (templating)
- **Backend**: Python (Flask or Django, as applicable)
- **Sentiment Analysis Library**: TextBlob (or any other library you are using)

## Installation

### Prerequisites
- Python 3.x installed on your system.
- A virtual environment setup is recommended.

### How to Use
1. Enter your text into the provided text area on the webpage.
2. Click the "Submit" button to analyze the text.
3. View the results, which include the sentiment classification, polarity, and subjectivity of your input text.

### Project Structure

sentiment-analysis-web-app/
├── app.py               # Main application logic
├── templates/           # HTML templates for the frontend
│   └── index.html       # Main page with the form and result display
├── static/              # Static files (CSS, JS, images, etc.)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

