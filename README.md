
# Email Spam Detection Web App

Modern, accessible, and visually appealing web application for detecting email spam using Python, Flask, and machine learning.

---

## 🚀 Overview

This project is a professional-grade Email Spam Detection web app that leverages a trained machine learning model to classify emails as "Spam" or "Not Spam". It features a modern, branded, and accessible user interface with multiple color themes, dark mode, prediction history, and interactive feedback—perfect for class presentations or real-world demos.

---

## ✨ Features

- **Machine Learning Powered**: Logistic Regression model with TF-IDF vectorization for robust spam detection.
- **Modern UI/UX**: Responsive design using Bootstrap, Google Fonts (Poppins), animated icons, and pastel color palette.
- **Multiple Color Themes**: Choose from Pastel, High Contrast, Teal, and Classic themes. Includes dark mode toggle with persistent user preference.
- **Accessibility**: High-contrast mode, ARIA labels, live regions, keyboard navigation, and readable text in all themes.
- **Prediction History**: View recent predictions in a table (CSV log for easy review).
- **User Feedback**: Toast notifications, loading spinner, and confetti animation for engagement.
- **Branding**: Custom logo, favicon, and a professional footer with copyright.
- **Touch-Friendly**: Optimized for both desktop and mobile devices.
- **Robust Backend**: Flask app with input validation, session-based feedback, and logging.

---

## 🖥️ Screenshots

> ![App Screenshot - Pastel Theme](src/static/screenshot_pastel.png)  
> ![App Screenshot - High Contrast](src/static/screenshot_contrast.png)

*(Add your own screenshots in `src/static/` and update the links above for your presentation!)*

---

## 📦 Project Structure

```
email-spam-detection/
├── README.md
├── requirements.txt
└── src/
    ├── app.py                # Flask web app (main entry point)
    ├── main.py               # CLI for model testing
    ├── train_model.py        # Model training script
    ├── prediction_log.csv    # Prediction history log
    ├── data/
    │   └── sample_emails.csv # Sample email data
    ├── models/
    │   └── spam_classifier.pkl # Trained ML model
    ├── static/
    │   ├── style.css         # Custom styles
    │   ├── favicon.ico       # Favicon
    │   ├── logo.png          # App logo
    │   └── Logo011.png       # Footer logo
    └── templates/
        └── index.html        # Main HTML template
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```powershell
   git clone https://github.com/Amel-saidy/email-spam-detection.git
   cd email-spam-detection
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **(Optional) Retrain the model**
   If you want to retrain the model with your own data:
   ```powershell
   python src/train_model.py
   ```
   This will update `src/models/spam_classifier.pkl`.

4. **Run the web app**
   ```powershell
   python src/app.py
   ```
   The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🕹️ Usage

1. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
2. Paste or type your email content in the input box.
3. Click **Check** to detect if the email is spam.
4. Switch color themes or toggle dark mode for accessibility and style.
5. View prediction results and history (CSV log).

---

## 🧩 Key Components

- **src/app.py**: Flask backend, handles prediction, session, and logging.
- **src/templates/index.html**: Main UI, theme selector, accessibility, and feedback features.
- **src/static/style.css**: All custom styles and theme overrides.
- **src/train_model.py**: Retrain or update the ML model.
- **src/data/sample_emails.csv**: Example emails for training/testing.
- **src/prediction_log.csv**: Stores prediction history for review.

---

## ♿ Accessibility & Presentation Notes

- **High Contrast & Readability**: All UI elements are readable in every theme, including high contrast and dark mode.
- **ARIA & Live Regions**: Alerts and notifications are accessible to screen readers.
- **Keyboard Navigation**: All controls are accessible via keyboard.
- **Branding**: Custom logo, favicon, and footer for a professional look.
- **Engagement**: Confetti and animation effects for user feedback.
- **Mobile Friendly**: Touch targets and layout optimized for mobile devices.

---

## 📝 License & Credits

- Developed by Amel Saidykhan, 2025
- [MIT License](LICENSE) *(add a LICENSE file if needed)*
- GitHub: [Amel-saidy/email-spam-detection](https://github.com/Amel-saidy/email-spam-detection)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork, submit PRs, or open issues.