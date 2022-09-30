#!/usr/bin/env python3

from pprint import pprint

import crayons
import requests

URL = "http://127.0.0.1:2224/json"

resp = requests.get(URL).json()

pprint(resp)

company = resp['Meta Data']['2. Symbol']
user_date = input("\nEnter the date in format (YYYY-MM-DD) you would like to check the stock performance: ")

if user_date.strip() in resp["Time Series (Daily)"]:
    stock_performance = resp["Time Series (Daily)"][user_date]
    print(
        f"\n{crayons.green('Here is how')} {crayons.red(company, bold=True)} {crayons.green('did on')} {crayons.magenta(user_date)}:")
    print(f"\n{crayons.cyan('Opened at:')} {crayons.yellow(stock_performance['1. open'])}"
          f"\n{crayons.cyan('High for the day:')} {crayons.yellow(stock_performance['2. high'])}"
          f"\n{crayons.cyan('Low for the day:')} {crayons.yellow(stock_performance['3. low'])}"
          f"\n{crayons.cyan('Closed at:')} {crayons.yellow(stock_performance['4. close'])}"
          f"\n{crayons.cyan('Total volume traded:')} {crayons.yellow(stock_performance['5. volume'])}")

else:
    print("There is no data for this date. The market was closed for weekend, or a holiday!")
