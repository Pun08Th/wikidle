from flask import Flask, render_template, request
import wikipedia as wiki
from logic import wordcount

app = Flask(__name__)

page = wiki.page("Barack Obama")
text = page.content

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        guess = request.form["guess"]
        # 👇 Replace this with your logic (e.g., count in article)
        result = wordcount(text, guess)
        return render_template("index.html", result=result, guess=guess)
    
    return render_template("index.html", result=None)
