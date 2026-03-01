from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import HEADLESS

def create_driver():
    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    return driver
