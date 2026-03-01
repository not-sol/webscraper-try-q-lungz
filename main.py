from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

search_item = input("Enter a product: ")
max_pages = int(input("Enter how many pages: "))

base_url = f"https://www.lazada.com.ph/tag/{search_item}"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")

print("Scraping...")
driver = webdriver.Chrome(options=options)

products = []

for page in range(1, max_pages + 1):

    if page == 1:
        url = base_url
    else:
        url = f"{base_url}/?page={page}"


    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.Bm3ON"))
    )

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    product_divs = soup.select("div.Bm3ON")

    for item in product_divs:
        # ---- NAME + LINK ----
        name = None
        link = None

        anchor = item.select_one("a[title]")
        if anchor:
            name = anchor.get("title")
            href = anchor.get("href")
            if href:
                if href.startswith("http"):
                    link = href
                else:
                    link = "https:" + href

        # ---- PRICE ----
        price_tag = item.select_one("span.ooOxS")
        price = price_tag.get_text(strip=True) if price_tag else None

        # ---- SOLD ----
        sold_tag = item.select_one("span._1cEkb")
        sold = sold_tag.get_text(strip=True) if sold_tag else None

        # ---- REVIEWS ----
        reviews_tag = item.select_one("span.qzqFw")
        reviews = reviews_tag.get_text(strip=True) if reviews_tag else None

        # ---- LOCATION ----
        location_tag = item.select_one("span.oa6ri")
        location = location_tag.get_text(strip=True) if location_tag else None

        # ---- STORE PRODUCT ----
        products.append({
            "name": name,
            "price": price,
            "sold": sold,
            "reviews": reviews,
            "location": location,
            "link": link,
        })

# ---- SAVE TO JSON ----
with open(f"data/{search_item}.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

print("Saved", len(products), "products to products.json")

driver.quit()
