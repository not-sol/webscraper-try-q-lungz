from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
from bs4 import BeautifulSoup

# SETTINGS
subreddit = "python"
target_post_count = 10

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0")

driver = webdriver.Chrome(options=options)
driver.get(f"https://www.reddit.com/r/{subreddit}/")
time.sleep(5)

# Scroll until enough content loads
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    articles = soup.find_all("article")

    print("Detected articles:", len(articles))

    if len(articles) >= target_post_count:
        break

driver.quit()

# Parse posts
collected_posts = []
seen_titles = set()

for article in articles:
    title_tag = article.find("h3")
    if not title_tag:
        continue

    title = title_tag.get_text(strip=True)

    if title in seen_titles:
        continue
    seen_titles.add(title)

    link_tag = article.find("a")
    link = link_tag["href"] if link_tag and link_tag.has_attr("href") else ""

    upvote_tag = article.select_one("[data-click-id='score']")
    upvotes = upvote_tag.get_text(strip=True) if upvote_tag else "N/A"

    collected_posts.append({
        "title": title,
        "link": link,
        "upvotes": upvotes
    })

    if len(collected_posts) >= target_post_count:
        break

# Save JSON
with open(f"{subreddit}_posts.json", "w", encoding="utf-8") as f:
    json.dump(collected_posts, f, indent=4, ensure_ascii=False)

print(f"Saved {len(collected_posts)} posts.")
