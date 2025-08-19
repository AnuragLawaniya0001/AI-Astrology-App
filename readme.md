🌌 AI Astrologer

A simple Flask web app that acts as an AI-powered astrologer.
Users enter their birth details (Name, Date, Time, Place) and can ask one free-text question. The app calculates their Zodiac sign and uses Google Gemini AI to generate personalized astrology readings and responses.

✨ Features

Collects user details: Name, Date of Birth, Time, Place

Automatically determines Zodiac sign from date of birth

Generates a personalized astrology reading (AI-driven)

Allows one free-text astrology question

Clean and minimal web UI (Flask + HTML)

🛠️ Tech Stack

Python 3

Flask – backend framework

HTML + CSS – frontend UI

Google Gemini AI – astrology responses

Rule-based utility – for zodiac sign calculation

📦 Installation

Clone this repository

git clone https://github.com/yourusername/ai-astrologer.git
cd ai-astrologer


Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install flask google-generativeai


Set your Gemini API key

export GEMINI_API_KEY="your_api_key_here"   # Mac/Linux
set GEMINI_API_KEY="your_api_key_here"     # Windows


Run the app

python app.py


Open in browser:
👉 http://127.0.0.1:5000

📂 Project Structure
ai-astrologer/
│── app.py              # Main Flask app
│── templates/
│   └── index.html      # Frontend HTML UI
│── README.md           # Project documentation

🔮 Example Flow

User enters:

Name: Anurag
Date of Birth: 2001-07-15
Time: 14:30
Place: Delhi
Question: Will I do well in my career?


App calculates zodiac → Cancer ♋

AI generates:

Astrology Reading about Cancer personality & energies

Career prediction response for the user’s question

🚀 Future Improvements

Add natal chart calculations

Support multiple free-text questions

Enhance UI with Bootstrap/Tailwind

Store user sessions in a database
