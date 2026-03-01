# Lazada Web Scraper 🛒

A Python-based web scraper that extracts product information from Lazada's search results. 

Since Lazada loads its products dynamically using JavaScript, this project uses a hybrid approach: **Selenium** drives a headless Chrome browser to load the page fully, and **BeautifulSoup** parses the HTML to extract the data efficiently.

## Features
* Bypasses basic bot detection using headless mode and specific Chrome flags.
* Handles pagination automatically based on user input.
* Extracts key product details: Name, Price, Items Sold, Reviews, Location, and Product Link.
* Saves the extracted data cleanly into a structured JSON file.
* Includes error handling for missing data elements (returns `None` instead of crashing).

## Installation

1. **Clone or download this repository** to your local machine.
2. **Open your terminal** and navigate to the project folder.
3. Create a virtual environment:**
```bash
python -m venv venv
```

Activate it with:
(Windows)
```bash
source venv\Scripts\activate
```

(Mac/Linux)
```bash
source venv/bin/activate
```
4. **Install the required Python libraries:**
   ```bash
   pip install selenium beautifulsoup4
   ```

## Usage

1. Run the script from your terminal:
   ```bash
   python main.py
   ```
2. The program will prompt you for two inputs:
   * **Enter a product:** Type the item you want to search for (e.g., `laptop`, `keyboard`, `shoes`).
   * **Enter how many pages:** Type the number of search result pages you want to scrape (e.g., `3`).
3. The script will run in the background (headless mode) and display a "Scraping..." message. 
4. Once finished, it will output the total number of products scraped and save them in a `data/` folder as a JSON file named after your search term (e.g., `data/laptop.json`).

## Sample Output

The resulting JSON file will look like this:

```json
[
    {
        "name": "Example Gaming Laptop 15.6 inch",
        "price": "₱45,000",
        "sold": "1.2K Sold",
        "reviews": "450 Reviews",
        "location": "Metro Manila",
        "link": "[https://www.lazada.com.ph/products/example-link](https://www.lazada.com.ph/products/example-link)..."
    }
]
```

## ⚠️ Important Disclaimer
E-commerce websites frequently update their user interfaces. The CSS selectors used in this script (e.g., `div.Bm3ON`, `span.ooOxS`) are auto-generated and highly likely to change in the future. If the script starts returning empty files or `None` for all values, you will need to inspect the Lazada webpage and update the selectors in the BeautifulSoup parsing section.

Please scrape responsibly and review the website's Terms of Service
