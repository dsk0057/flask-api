#!/usr/bin/env python3

from pprint import pprint
import crayons
import requests

# flask api url so that we can use it to display some data
URL = "http://127.0.0.1:2224/json"

# get the data from api in json format
resp = requests.get(URL).json()

# use pprint to print data in a prettier format
pprint(resp)

# get the symbol from the returned json
company = resp['Meta Data']['2. Symbol']
# ask user to enter date in the provided format
user_date = input("\nEnter the date in format (YYYY-MM-DD) you would like to check the stock performance: ")

# normalize the input and display data using crayons for color
# if the date provided by user exists in the json object, then display the data
if user_date.strip() in resp["Time Series (Daily)"]:
    stock_performance = resp["Time Series (Daily)"][user_date]
    print(
        f"\n{crayons.green('This is how')} {crayons.red(company, bold=True)} {crayons.green('did on')} {crayons.magenta(user_date)}:")
    print(f"\n{crayons.cyan('Opened at:')} {crayons.yellow(stock_performance['1. open'])}"
          f"\n{crayons.cyan('High for the day:')} {crayons.yellow(stock_performance['2. high'])}"
          f"\n{crayons.cyan('Low for the day:')} {crayons.yellow(stock_performance['3. low'])}"
          f"\n{crayons.cyan('Closed at:')} {crayons.yellow(stock_performance['4. close'])}"
          f"\n{crayons.cyan('Total volume traded:')} {crayons.yellow(stock_performance['5. volume'])}")
# otherwise, let user know there is no data for the provided date
else:
    print("There is no data for this date. The market was closed for weekend, or a holiday!")
