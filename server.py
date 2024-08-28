"""This is the server for emotion detection application"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows the dominant emotion.
    '''
    input_text = request.args.get('textToAnalyze')
    res = emotion_detector(input_text)
    if res is None:
        return "Invalid input! Try again."
    anger = res.get('anger', 0)
    disgust = res.get('disgust', 0)
    fear = res.get('fear', 0)
    joy = res.get('joy', 0)
    sadness = res.get('sadness', 0)
    dominant_emotion = res.get('dominant_emotion', 'Unknown')
    if dominant_emotion is None:
        return "Invalid text! Please try again"
    return(f"For the given statement,"
    f" the system response is 'anger': {anger}, 'disgust': {disgust},"
    f"'fear': {fear}, 'joy': {joy},"
    f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
