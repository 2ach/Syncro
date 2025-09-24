from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import requests
import random
import csv
import re

WEBDRIVER_EXE = r'C:\Users\Zach_Schulz-Behrend\dev\webdriver\edgedriver_win64\msedgedriver.exe'

class SalesChatWebDriver:
    def __init__(self, link):
        self.link = link
        self.store = r'C:\Users\Zach_Schulz-Behrend\dev\Syncro\\'
        num_of_prompts = random.randint(3, 12)

        prompt = "Create {0} bullets as prompts. No formatting, just text. Make each bullet/prompt applicable to the latest internal " \
        "information and documentation as of today. The goal is to make {0} unique prompts without sounding redundant. " \
        "Good examples have the latest 411/911 information, new product details, and EOL data. All good examples have data sources. " \
        "for the information. Bad examples are sample questions to ask a customer and general sales questions. " \
        "Prompts should not end in a question.".format(num_of_prompts)

        self.gen_prompt = prompt

    def open_page(self):
        service = webdriver.EdgeService(executable_path=WEBDRIVER_EXE)
        options = webdriver.EdgeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get(self.link)
        self.wait = WebDriverWait(self.driver, 600)

    def send_prompt(self, prompt=None):
        if prompt == None:
            prompt = self.gen_prompt
        else:
            prompt = prompt 
        
        self.wait.until(EC.element_to_be_clickable((By.ID, "chat-input")))
        self.driver.find_element(By.XPATH, '//div[@contenteditable="true" and @role="textbox"]').send_keys(prompt)
        self.driver.find_element(By.ID, "chat-send-button").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and @aria-label="Send" and @id="chat-send-button"]')))
    

    def scrape_prompts(self):
        r = self.driver.page_source
        soup = BeautifulSoup(r, 'html.parser')
        assistant_response = soup.find('pre', attrs={'aria-label': 'Assistant Response'})
        self.prompts = []
        for para in assistant_response.find_all('p'):
                self.prompts.append(para.get_text(strip=True))
    
    def save_prompts(self):
        with open(self.store + 'output_prompts.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for item in self.prompts:
                writer.writerow([item])