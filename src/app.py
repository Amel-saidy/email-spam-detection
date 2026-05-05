from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import os
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'spam_classifier.pkl')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

vectorizer, model = joblib.load(MODEL_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    email_content = ''
    error = None
    MAX_LENGTH = 1000
    if request.method == 'POST':
        email_content = request.form.get('email_content', '')
        # Limit length
        if len(email_content) > MAX_LENGTH:
            error = f"Input too long (max {MAX_LENGTH} characters)."
        else:
            # Sanitize HTML
            email_content = re.sub(r'<.*?>', '', email_content)
            processed = preprocess_text(email_content)
            email_vec = vectorizer.transform([processed])
            pred = model.predict(email_vec)[0]
            prediction = 'Spam' if pred == 1 else 'Not Spam'
            # Logging
            log_path = os.path.join(os.path.dirname(__file__), 'prediction_log.csv')
            import csv
            from datetime import datetime
            with open(log_path, 'a', newline='', encoding='utf-8') as logfile:
                writer = csv.writer(logfile)
                if logfile.tell() == 0:
                    writer.writerow(['timestamp', 'email_content', 'prediction'])
                writer.writerow([
                    datetime.now().isoformat(),
                    email_content.replace('\n', ' ').replace('\r', ' '),
                    prediction
                ])
            # Store results in session and redirect
            session['prediction'] = prediction
            session['email_content'] = email_content
            session['error'] = error
            return redirect(url_for('index'))
    else:
        prediction = session.pop('prediction', None)
        email_content = session.pop('email_content', '')
        error = session.pop('error', None)
    return render_template('index.html', prediction=prediction, email_content=email_content, error=error)

if __name__ == '__main__':
    app.run(debug=True)
