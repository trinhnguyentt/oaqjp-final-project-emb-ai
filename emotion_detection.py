import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
 
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting the required set of emotions from the response
    emotion = formatted_response["emotionPredictions"][0]["emotion"]
    dominant = max(emotion, key=emotion.get)
   
    return {
    'anger': emotion.get('anger'),
    'disgust': emotion.get('disgust'),
    'fear': emotion.get('fear'),
    'joy': emotion.get('joy'),
    'sadness': emotion.get('sadness'),
    'dominant_emotion': dominant
   }    #return response.text 