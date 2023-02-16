from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    navn = "Hjem"
    return render_template("index.html", navn=navn)

@app.route("/onsker")
def index():
    navn = "Ønsker å lese"
    return render_template("onsker.html", navn=navn)

@app.route("/lest")
def index():
    navn = "Leste bøker"
    return render_template("lest.html", navn=navn)

app.run(debug=True)