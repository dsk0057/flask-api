#!/usr/bin/python3

from datetime import date

import requests
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=YAT8ZYQBD2YA3SVF'

app = Flask(__name__)


@app.route("/<name>")
def welcome(name):
    return render_template("welcome.html", name=name)


@app.route("/stock")
def stock():
    return render_template("stock.html")


@app.route("/json")
def get_json():
    # return jsonify(requests.get(url).json())
    data = requests.get(url).json()
    return data


# This is a landing point for users (a start)
@app.route("/")  # user can land at "/"
def start():
    return render_template("welcome.html")  # look for templates/postmaker.html


# This is where welcome.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/enter_info", methods=["POST", "GET"])
def login():
    global symbol, url
    # POST would likely come from a user interacting with welcome.html
    if request.method == "POST":
        if request.form.get("sym"):  # if sym was assigned via the POST
            symbol = request.form.get("sym").upper()  # grab the value of sym from the POST
        else:  # if a user sent a post without sym then assign value defaultuser
            symbol = "AAPL"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("sym"):  # if sym was assigned as a parameter=value
            symbol = request.args.get("sym").upper()  # pull sym from localhost:5060/login?sym=larry
        else:  # if sym was not passed...
            symbol = "AAPL"  # ...then symbol is AAPL
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=YAT8ZYQBD2YA3SVF'
    return redirect(url_for("get_json"))  # pass back to /success with val for name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
