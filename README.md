# auto-lotto
Automatically enrol into a [free-lottery](https://www.lottery.co.uk/free-lottery) ticket.

## Requirement

- lottery.co.uk [account](https://www.lottery.co.uk/account/register)
- Python 3.X


## Installation

Use the package manager to install requirements.

```bash
pip install -r requirements.txt
```

## Create `.env` file

**[required]** Add account details in `.env` file
- EMAIL : login email
- PASSWORD : login password

**(optional)** Add any of the following details in `.env` file
- LUCKYNUM : 
  - predefined lucky number to enrol in ticket
  - space-seperated
  - max 6 number
  - remaining number in the ticket is randomly selected
  - remove the whole line if no lucky number
- DRIVERPATH : 
  - if `chrome` is not installed on the system, additional driver is needed
  - remove the whole line if `chrome` is already installed
  
```.env
EMAIL='my.login@email.com'
PASSWORD='Mypassw0rd.'
LUCKYNUM='9 27'
DRIVERPATH='./chromedriver'
```

## Driver
Download driver from [here](https://sites.google.com/chromium.org/driver/) if `chrome` is not installed 
