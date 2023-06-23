# free-lotto-bot
Automatically enrol into a [free-lottery](https://www.lottery.co.uk/free-lottery) ticket with a single commonad.

## Technologies
- **Language** : Python
- **Package** : Selenium


## Create `.env` file

**[required]** Add _lottery.co.uk_ [account](https://www.lottery.co.uk/account/register) details in `.env` file
- EMAIL : login email
- PASSWORD : login password

**(optional)** Add any of the following details in `.env` file
- LUCKYNUM : 
  - predefined lucky number to enrol in ticket
  - space-seperated
  - max 6 number
  - remaining number in the ticket is randomly selected
  - Do not add this if no lucky number is needed
- DRIVERPATH : 
  - if `chrome` is not installed on the system, additional driver is needed
  - Do not add this if `chrome` is already installed
  
```.env
EMAIL='my.login@email.com'
PASSWORD='Mypassw0rd.'
LUCKYNUM='9 27'
DRIVERPATH='./chromedriver'
```

## Driver
Download driver from [here](https://sites.google.com/chromium.org/driver/) if `chrome` is not installed 

## Usage
```
python main.py
```

