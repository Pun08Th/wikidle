from flask import Flask, render_template, request, session
import wikipedia as wiki
from logic import wordcount
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key")

# Fixed article
page = wiki.page("Barack Obama")
text = page.content
actual_title = page.title.lower()  # So we can check against guesses later

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize session data
    if "guesses" not in session:
        session["guesses"] = []

    result = None
    guess = ""
    article_feedback = None

    if request.method == "POST":
        if "guess" in request.form:
            guess = request.form["guess"]
            count = wordcount(text, guess)
            session["guesses"].append((guess, count))
            session.modified = True  # Required to update session list
        elif "article_guess" in request.form:
            article_guess = request.form["article_guess"].lower()
            if article_guess == actual_title:
                article_feedback = "🎉 Correct! You guessed the article!"
            else:
                article_feedback = f"❌ '{article_guess}' is not the article."

    return render_template(
        "index.html",
        result=result,
        guess=guess,
        guesses=session["guesses"],
        article_feedback=article_feedback
    )

