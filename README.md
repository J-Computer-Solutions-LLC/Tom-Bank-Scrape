# Tom-Bank-Scrape(Bot)

## Configuring Bot to run using your credintials

Fill out config.json file with info:

    - First Name
    - Middle Name or Initial
    - Last Name
    - Suffix
  
Leave blank if doesn't apply

## Adding webdriver for Selenium to run on your machine

Check your browser version by selecting the hamburger menu in the top right-hand corner of your 
browser, then at the bottom of the menu select help then about browser.

You can download your specific webdriver to your web-browser by going to:

Chrome Driver: https://sites.google.com/a/chromium.org/chromedriver/downloads
Firefox Driver: https://github.com/mozilla/geckodriver/releases

Add $PATH to your webdriver in json.config where stated in the same format as the example.
If using Firefox everthing stays the same except you'll need to change in main.py under init function
self.driver = driver.Chrome to self.driver = driver.Firefox.

## Add more banks to bot

Create a new function ( I name the function after the bank name for ease of navigation )
Follow the format of the previous bank functions:

    - self.driver.get('url to Credit Card Application page')
    - driver.find.element by("the best name of the html element for the field where you would put your credintials")
        * I use the input id tag name but sometimes the xpath works better, its all trial and error
        * send keys based on what field you wish to fill
    -find the xpath to the submit button and name it as a variable "refer to other bank functions for example"
    - varible name( submitButton.click() ) "refer to other bank functions for example"
    - 
Last within apply function add call-to-new-bank-function ( self.newBankFuntion() ) to run it.
