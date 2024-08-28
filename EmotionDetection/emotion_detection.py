
"""This function connects to watson emotion prediction API"""
import requests
import json

def emotion_detector(text_to_analyze):
    """emotion_detector function to connect to watson emotion prediction API. Takes a text and analyses it to predict the emotion around it and returns to result to the user"""
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response = response.text
    format_response = json.loads(response)
    emotion_prediction = format_response['emotionPredictions'][0]['emotion']

    anger_score = emotion_prediction.get('anger', 0)
    disgust_score = emotion_prediction.get('disgust', 0)
    fear_score = emotion_prediction.get('fear', 0)
    joy_score = emotion_prediction.get('joy', 0)
    sadness_score = emotion_prediction.get('sadness', 0)

    max_score = 0
    max_emotion = None
    for emotion, score in emotion_prediction.items():
        if score > max_score:
            max_score = score
            max_emotion = emotion

    score_rate = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': max_emotion
    }
    return score_rate
