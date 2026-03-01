from driver import create_driver
from scraper import scrape_pages
from utils import save_to_json

def main():
    search_item = "-".join(input("Enter a product: ").strip().split())
    max_pages = int(input("Enter how many pages: "))

    print("Scraping...")

    driver = create_driver()

    try:
        products = scrape_pages(driver, search_item, max_pages)
        save_to_json(search_item, products)

        print(f"Saved {len(products)} products to data/{search_item}.json")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
