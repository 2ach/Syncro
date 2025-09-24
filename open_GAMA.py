from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

WEBDRIVER_EXE = r'..\webdriver\edgedriver_win64\msedgedriver.exe'
# r'C:\Users\Zach_Schulz-Behrend\AppData\Roaming\Python\Python312\site-packages\selenium\webdriver\edge\msedgedriver.exe'
sales_rep_id = "256656"

def open_page(link):
    service = webdriver.EdgeService(executable_path=WEBDRIVER_EXE)
    options= webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.get(link)
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "I Agree"))).click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sales Rep"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "sa_compID175"))).send_keys(sales_rep_id)
    wait.until(EC.element_to_be_clickable((By.ID, "sa_compID186"))).click()
    

    scrape_accts(driver)
    # driver.quit()

    return None

def scrape_accts(driver):
    r = driver.page_source
    soup = BeautifulSoup(r, 'html.parser')


    return None

def main():
    link = 'https://dstweb.us.dell.com/gama#/Home'
    open_page(link)


if __name__ == "__main__":
    main()