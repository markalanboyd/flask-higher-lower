import random

from flask import Flask
from pathlib import Path

app = Flask(__name__)
home = Path("home.html").read_text()
too_high = Path("too-high.html").read_text()
too_low = Path("too-low.html").read_text()
correct = Path("correct.html").read_text()

random_int = random.randint(0, 9)
print(random_int)


@app.route("/")
def home_page():
    return home


@app.route("/<int:number>")
def correct_page(number):
    if number == random_int:
        return correct
    if number > random_int:
        return too_high
    else:
        return too_low


app.run(debug=True)
