from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)


genai.configure(api_key=os.getenv("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))
model = genai.GenerativeModel("gemini-1.5-flash")


def get_zodiac_sign(day: int, month: int) -> str:
    zodiac_dates = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
    ]
    for sign, (sm, sd), (em, ed) in zodiac_dates:
        if (month == sm and day >= sd) or (month == em and day <= ed):
            return sign
    return "Capricorn"


@app.route("/", methods=["GET", "POST"])
def index():
    reading, qna = None, None
    if request.method == "POST":
        name = request.form["name"]
        birth_date = request.form["birth_date"]  # yyyy-mm-dd
        birth_time = request.form["birth_time"]
        birth_place = request.form["birth_place"]
        question = request.form["question"]

        year, month, day = map(int, birth_date.split("-"))
        sign = get_zodiac_sign(day, month)

        # Astrology reading
        prompt = f"""
        You are an AI astrologer. Give a short, warm astrology reading for:
        Name: {name}
        DOB: {birth_date} Time: {birth_time}
        Place: {birth_place}
        Zodiac Sign: {sign}
        """
        reading = model.generate_content(prompt).text

        
        if question.strip():
            qna_prompt = f"""
            Astrology Q&A:
            Person: {name}, Sign: {sign}
            Question: {question}
            Give an astrology-style answer.
            """
            qna = model.generate_content(qna_prompt).text

    return render_template("index.html", reading=reading, qna=qna)


if __name__ == "__main__":
    app.run(debug=True)
