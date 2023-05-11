from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time
import random
import os
import json
from dotenv import load_dotenv

load_dotenv()

login_actions = [
    ("panelButton", "click"),
    ("Email0", os.getenv('EMAIL')),
    ("Password0", os.getenv('PASSWORD')),
    ("submit_login_details", "click")
]

enroll_actions =[]
def form_choice():
    choice = [int(n) for n in os.environ.get("LUCKYNUM").split(" ")]
    choices = []
    for i in range(1,76):
        i not in choice and choices.append(i)
    rnd = random.sample(choices, 6-len(choice))
    choice.extend(rnd)
    return sorted(choice)
def choice2action(choice):
    for n in choice:
        enroll_actions.append((f"B0ID_{n}", "click"))

def do_login(web):
    print(f"DO : LOGIN")
    web.go_to("https://www.lottery.co.uk/free-lottery")
    web.do_actions(login_actions)
    print()

def do_enrol(web):
    choice = form_choice()
    print(f"DO : ENROL - {choice}")
    choice2action(choice)
    web.go_to("https://www.lottery.co.uk/free-lottery/play?lottery=daily")
    try:
        enable = web.driver.find_element(By.ID, 'submit_ticket').is_enabled()
        web.do_actions(enroll_actions)
        web.do_action('submit_ticket', 'click')
        print()
    except NoSuchElementException:
        print('UNABLE TO ENROL')

class LottoWeb(object):
    def __init__(self) -> None:
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
    
    def go_to(self, url):
        self.driver.get(url)

    def do_actions(self, action_list):
        for item in action_list:
            eid = item[0]
            action = item[1]
            self.do_action(eid, action)
    
    def do_action(self, eid, action):
        element = self.driver.find_element(By.ID,eid)
        if action == 'click':
            element.click()
        else:
            element.send_keys(action)
        print(f"action : {eid:<20} | {action}")

if __name__ == '__main__':
    web = LottoWeb()
    do_login(web)
    time.sleep(0.5)
    do_enrol(web)
    