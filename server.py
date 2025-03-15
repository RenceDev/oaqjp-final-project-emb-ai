"""
Flask application for emotion detection.

This module sets up a simple web application using Flask to perform emotion
detection on a given text input. It exposes one route for text analysis and
returns the emotion prediction in a human-readable format.
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index page of the application.
    
    Returns:
        Response: The rendered HTML page (index.html).
    """
    return render_template('index.html')  # Render the index.html page

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Endpoint to analyze the text and detect emotions.
    
    This function receives text input from the user and returns a response
    with emotion detection results in the specified format.
    
    Returns:
        Response: A JSON object with the system response or an error message if input is invalid.
    """
    # Get the text to analyze from the request
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        # Handle blank input
        return jsonify({"error": "No text provided"}), 400

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        # Handle case where no dominant emotion was detected
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Prepare the response string in the desired format
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify(response=response)


if __name__ == '__main__':
    """
    Run the Flask application in debug mode on all interfaces (0.0.0.0), 
    making it accessible on port 5000.
    """
    app.run(debug=True, host='0.0.0.0', port=5000)
