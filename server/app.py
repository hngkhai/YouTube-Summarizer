from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from summarize_youtube import summarize_youtube_video
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Root route
@app.route('/')
def home():
    return "Welcome to the YouTube Summarizer! Use the /summarize endpoint to get a summary."

# Summarize route
@app.route('/summarize', methods=['POST', 'OPTIONS'])  # Allow OPTIONS requests
def summarize():
    if request.method == 'OPTIONS':
        # Handle preflight requests
        response = jsonify({'message': 'Preflight request allowed'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    # Handle POST requests
    data = request.json
    video_url = data['url']
    summary = summarize_youtube_video(video_url)
    print (summary)
    response = jsonify({'summary': summary})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(port=5000)