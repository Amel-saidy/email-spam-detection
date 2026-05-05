import joblib
import os
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

def load_model(model_path):
    if not os.path.exists(model_path):
        print(f"Model file not found at {model_path}")
        return None, None
    try:
        vectorizer, model = joblib.load(model_path)
        return vectorizer, model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None

def predict_spam(vectorizer, model, email_content):
    if vectorizer is None or model is None:
        return None
    try:
        email_content = preprocess_text(email_content)
        email_vec = vectorizer.transform([email_content])
        prediction = model.predict(email_vec)
        return prediction[0]
    except Exception as e:
        print(f"Error predicting spam: {e}")
        return None

def main():
    model_path = 'src/models/spam_classifier.pkl'
    vectorizer, model = load_model(model_path)
    if vectorizer is None or model is None:
        return

    print("Enter an email to check if it's spam or not (type 'exit' to quit):")
    while True:
        email_content = input("\nEmail: ")
        if email_content.lower() == 'exit':
            print("Exiting... Goodbye!")
            break
        if not email_content.strip():
            print("Input cannot be empty.")
            continue
        prediction = predict_spam(vectorizer, model, email_content)
        if prediction is not None:
            label = 'Spam' if prediction == 1 else 'Not Spam'
            print(f"Prediction: {label}")

if __name__ == '__main__':
    main()

    
    
"""import pandas as pd
import joblib

def load_model(model_path):
    try:
        vectorizer, model = joblib.load(model_path)
        return vectorizer, model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None

def predict_spam(vectorizer, model, email_content):
    if vectorizer is None or model is None:
        return None
    try:
        email_vec = vectorizer.transform([email_content])
        prediction = model.predict(email_vec)
        return prediction[0]
    except Exception as e:
        print(f"Error predicting spam: {e}")
        return None

def main():
    model_path = 'src/models/spam_classifier.pkl'
    vectorizer, model = load_model(model_path)
    if vectorizer is None or model is None:
        return

    # Load sample emails for testing
    sample_emails = pd.read_csv('src/data/sample_emails.csv')

    for index, row in sample_emails.iterrows():
        email_content = row['email']
        prediction = predict_spam(vectorizer, model, email_content)
        if prediction is not None:
            label = 'Spam' if prediction == 1 else 'Not Spam'
            print(f'Email: {email_content}\nPrediction: {label}\n')

if __name__ == '__main__':
    main()"""
