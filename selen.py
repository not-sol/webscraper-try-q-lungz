from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

from human_pattern import human_pause, human_scroll  # 👈 import here

# -----------------------
# SETTINGS
# -----------------------
SUBREDDIT_URL = "https://www.reddit.com/r/Python/"
MAX_POSTS = 10

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get(SUBREDDIT_URL)

if "captcha" in driver.page_source.lower():
    print("⚠ CAPTCHA detected on subreddit page.")
    input("Solve CAPTCHA manually, then press Enter to continue...")

# Wait for articles
wait.until(EC.presence_of_element_located((By.TAG_NAME, "article")))

# 👇 Human-like behavior after loading page
human_pause()
human_scroll(driver)
human_pause()

# Parse page
soup = BeautifulSoup(driver.page_source, "html.parser")
articles = soup.find_all("article")

post_links = []

for article in articles:
    if len(post_links) >= MAX_POSTS:
        break  # 🔥 stop once we have enough

    a_tag = article.find("a")
    if a_tag and a_tag.get("href"):
        full_link = urljoin("https://www.reddit.com", a_tag["href"])
        if full_link not in post_links:
            post_links.append(full_link)

print(f"Visiting {len(post_links)} posts")

# Visit posts
for idx, link in enumerate(post_links):
    print(f"\nVisiting post {idx+1}")

    driver.get(link)
    human_pause(3, 6)   # 👈 simulate reading time

    try:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[data-test-id='post-content']")
        ))
        print("✅ Loaded successfully")
    except:
        print("❌ Failed to load")

    # Simulate reading scroll
    human_scroll(driver)

    human_pause(2, 4)
    driver.back()

    human_pause(2, 4)

driver.quit()
