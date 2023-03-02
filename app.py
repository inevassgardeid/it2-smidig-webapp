from flask import Flask, render_template
from books import hent_books

app = Flask(__name__)

bokliste = hent_books()

@app.route("/")
def index():
    navn = "Hjem"
    return render_template("index.html")

@app.route("/boker")
def rute_boker():
    navn = "Bøker"
    print(bokliste)
    return render_template("boker.html", bokliste=bokliste)

@app.route("/onsker")
def rute_onsker():
    navn = "Ønsker å lese"
    return render_template("onsker.html", navn=navn)

@app.route("/lest")
def rute_lest():
    navn = "Leste bøker"
    return render_template("lest.html", navn=navn)

app.run(debug=True)