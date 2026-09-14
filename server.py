"""
 Deploy as web application using Flask
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app by the name "Emotion Detector"
app = Flask("Emotion Detector")

# Set end point for calling emotion detector function
@app.route("/emotionDetector")
def emo_detector():
    """
    Process an emotion‑analysis request by extracting the input text, running the
    emotion detection model, and returning a formatted summary of the results.

    The function performs the following steps:
    - Retrieves the text to analyze from the request query parameter `textToAnalyze`.
    - Passes the text to `emotion_detector()` to obtain emotion scores and the
      dominant emotion.
    - Extracts individual emotion values (anger, disgust, fear, joy, sadness) and
      the dominant emotion from the response.
    - Validates the response; if the emotion label is missing, returns an error
      message.
    - Returns a human‑readable formatted string describing all emotion scores and
      the detected dominant emotion.

    Returns:
        str: A formatted message containing emotion scores and the dominant
        emotion, or an error message if the input is invalid.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the result from the response
    emotion =  response['emotion']
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    # Return a formatted string with the response
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the HTML template using render_index_page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
