#!/usr/bin/python3
'''Flask Project that displays stock data'''

import requests
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

# The url for stock info assigned to url variable
# symbol has been assigned 'AAPL' as the default value
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=YAT8ZYQBD2YA3SVF'

app = Flask(__name__)


# This route displays a welcome message with person's name
@app.route("/<name>")
def welcome(name):
    return render_template("welcome.html", name=name)


# this route takes you to the page where you can input stock symbol for data
@app.route("/stock")
def stock():
    return render_template("stock.html")


# this is where the api call happens and data is returned in json() format
@app.route("/json")
def get_json():
    data = requests.get(url).json()
    return data


# This is a landing point for users
@app.route("/")
def start():
    return render_template("welcome.html")  # look for templates/postmaker.html


# This is where welcome.html POSTs data to
# Or a user can also browser (GET) to this location
@app.route("/enter_info", methods=["POST", "GET"])
def enter():
    global symbol, url
    # POST would likely come from a user interacting with welcome.html
    if request.method == "POST":
        if request.form.get("sym"):  # if sym was assigned via the POST
            symbol = request.form.get("sym").upper()  # grab the value of sym from the POST
        else:  # if a user sent a post without sym then assign value "AAPL"
            symbol = "AAPL"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("sym"):  # if sym was assigned as a parameter=value
            symbol = request.args.get("sym").upper()
        else:  # if sym was not passed...
            symbol = "AAPL"  # ...then symbol is AAPL
    # the url now is getting a symbol from user and replacing it in the api for call
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=YAT8ZYQBD2YA3SVF'
    return redirect(url_for("get_json"))  # pass back to /json to display the data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
