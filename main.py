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

def do_login(web):
    print(f"DO : LOGIN")
    web.go_to("https://www.lottery.co.uk/free-lottery")
    web.do_actions(web.login_actions)
    print()

def do_enrol(web):
    print(f"DO : ENROL - {web.choice}")
    web.go_to("https://www.lottery.co.uk/free-lottery/play?lottery=daily")
    try:
        enable = web.driver.find_element(By.ID, 'submit_ticket').is_enabled()
        web.do_actions(web.enroll_actions)
        web.do_action('submit_ticket', 'click')
    except NoSuchElementException:
        print('UNABLE TO ENROL')
    print()

def do_weekly(web):
    print(f"DO : WEEKLY - {web.choice}")
    web.go_to("https://www.lottery.co.uk/free-lottery/play?lottery=weekly")
    try:
        enable = web.driver.find_element(By.ID, 'submit_ticket').is_enabled()
        web.do_actions(web.enroll_actions)
        web.do_action('submit_ticket', 'click')
        enroll_actions =[]
    except NoSuchElementException:
        print('UNABLE TO ENROL')
    print()

class LottoWeb(object):
    def __init__(self) -> None:
        options = Options()
        # options.add_experimental_option("detach", True)
        options.add_argument("--headless")
        exe = os.getenv('DRIVERPATH', False)
        print(f"EXE : {exe}\n")
        if not exe:
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = webdriver.Chrome(exe, options=options)

        self.login_actions = [
            ("panelButton", "click"),
            ("Email0", os.getenv('EMAIL')),
            ("Password0", os.getenv('PASSWORD')),
            ("submit_login_details", "click")
        ]
        self.choice = self.gen_choice()
        self.enroll_actions = [(f"B0ID_{n}", "click") for n in self.choice]
    
    def go_to(self, url):
        self.driver.get(url)

    def do_actions(self, action_list):
        for item in action_list:
            eid = item[0]
            action = item[1]
            self.do_action(eid, action)
    
    def do_action(self, eid, action):
        actionC = ActionChains(self.driver)
        element = self.driver.find_element(By.ID,eid)
        if action == 'click':
            actionC.move_to_element(element).click().perform()
        else:
            element.send_keys(action)
        print(f"action : {eid:<20} | {action}")

    def gen_choice(self):
        LUCKYNUM = os.getenv('LUCKYNUM', False)
        print(f"LUCKNUM : {LUCKYNUM}\n")
        if not LUCKYNUM:
            choice = []
        else:
            choice = [int(n) for n in LUCKYNUM.split(" ")]
        choices = []
        for i in range(1,76):
            i not in choice and choices.append(i)
        rnd = random.sample(choices, 6-len(choice))
        choice.extend(rnd)
        return sorted(choice)

if __name__ == '__main__':
    web = LottoWeb()
    do_login(web)
    ## wait 0.5 sec for website redirection
    time.sleep(0.5)
    do_enrol(web)
    do_weekly(web)