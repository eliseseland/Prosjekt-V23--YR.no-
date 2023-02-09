from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bergen")
def rute_bergen():
    return render_template("bergen.html")


@app.route("/kristiansand")
def rute_kristiansand():
    return render_template("kristiansand.html")


@app.route("/oslo")
def rute_oslo():
    return render_template("oslo.html")


@app.route("/sandvika")
def rute_sandvika():
    return render_template("sandvika.html")

@app.route("/tromsø")
def rute_tromsø():
    return render_template("tromsø.html")

