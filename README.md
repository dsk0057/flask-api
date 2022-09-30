# flask-api

***This was built and tested in pycharm. I have not tested with curl command***

Here is the gist of the project:

# alta3research-flask01.py
- The initial load takes a user to the welcome page(welcome.html). If someone enters their name, it will welcome with the name via /<name> route.
- stock.html extends welcome.html, where user can click on a link to go to stock page via /stock route.
- /json route gets data by calling external API and returning json object.
- /enter_info route is where the conditions are checked for "POST" and "GET". Also, grabs the user input and dynamically inserts that into url to get the json object for that particular input.
  
# alta3research-requests02.py
- The flask API has been defined here.
- json object is got using requests.
- using pprint(), the data is displayed.
- user is asked to input a date for which they want the stock data.
- The input is normalized and the data is displayed in colorful text using crayons with the data call from flask API.
  
If the first script is ran and entered a symbol, then when second script is ran, after user inputs desired date, the data is displayed for the symbol that was entered in the first script for the date user entered in the second script.
  
