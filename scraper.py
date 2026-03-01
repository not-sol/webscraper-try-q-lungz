from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import WAIT_TIMEOUT, BASE_URL
from parser import parse_products


def scrape_pages(driver, search_item, max_pages):
    all_products = []

    for page in range(1, max_pages + 1):

        if page == 1:
            url = f"{BASE_URL}{search_item}"
        else:
            url = f"{BASE_URL}{search_item}/?page={page}"

        driver.get(url)

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.Bm3ON"))
        )

        html = driver.page_source
        products = parse_products(html)
        all_products.extend(products)

    return all_products
