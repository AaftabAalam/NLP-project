import torch
from transformers import pipeline


sentiment_analyzer = pipeline("sentiment-analysis")
emotion_analyzer = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")


def analyze_messages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        messages = file.readlines()


    for message in messages:
        message = message.strip()
        if message:  
            sentiment_result = sentiment_analyzer(message)[0]
            sentiment_label = sentiment_result['label']
            sentiment_score = sentiment_result['score']

            emotion_result = emotion_analyzer(message)[0]
            emotion_label = emotion_result['label']
            emotion_score = emotion_result['score']

            print(f"\nMessage: {message}")
            print(f"Sentiment: {sentiment_label} (Score: {sentiment_score:.2f})")
            print(f"Emotion: {emotion_label} (Score: {emotion_score:.2f})")
            print("-" * 50)

text_file_path = '/Users/apple/ml-setup/ML/NLP work1/sentences.txt' # The sentences.txt path
analyze_messages(text_file_path)
