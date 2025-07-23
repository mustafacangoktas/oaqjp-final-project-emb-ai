"""
Flask server module for emotion detection application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the homepage with the input form.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Handle emotion detection request.
    Extracts text from query parameters, passes it to the emotion detector, and returns the formatted response.
    """
    text = request.args.get('textToAnalyze', '')

    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
