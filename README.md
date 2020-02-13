# InstagramBot
InstagramBot using python and Selenium.

## About:

This bot will return a python list of all users that you FOLLOW but do NOT follow back. The bot automates the process, by going into your followers list and returning list of user names in there and doing the same to the list of user accounts in following list. Then the code will do a comparison between names in following and followers list, and return a final list of user accounts that you follow but dont follow you back.


## Requirements:
- python3
- selenium chrome driver
- must install virtualenv (most work will be done there)


### Once you have all the requirments set up, run commands in this order:
#### Setup enviroment:
  `virtualenv -p python3 venv`
  
#### Activate environment:
  `source venv/bin/activate`
  
#### Finally once you have all the code in main.py, run it:
  `python3 main.py`
  
  
### IMPORTANT NOTES:
- Insert username & password on line 93. replace the text INSERT USERNAME HERE & INSERT PASSWORD HERE, with your own passwords AND keep single quotations around the text.

- Save main.py inside of te project folder.
