import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()

        # Check if status_code is 400 (bad request)
        if response.status_code == 400:
            # Return None for all keys if response is bad
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        # Process and extract relevant emotion data
        emotions = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
        dominant_emotion = max(emotions, key=emotions.get) if emotions else None

        return {
            "anger": emotions.get('anger'),
            "disgust": emotions.get('disgust'),
            "fear": emotions.get('fear'),
            "joy": emotions.get('joy'),
            "sadness": emotions.get('sadness'),
            "dominant_emotion": dominant_emotion
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
