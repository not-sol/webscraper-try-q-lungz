from bs4 import BeautifulSoup

def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")
    product_divs = soup.select("div.Bm3ON")

    products = []

    for item in product_divs:
        name = None
        link = None

        anchor = item.select_one("a[title]")
        if anchor:
            name = anchor.get("title")
            href = anchor.get("href")
            if href:
                link = href if href.startswith("http") else "https:" + href

        price_element = item.select_one("span.ooOxS")
        price = price_element.get_text(strip=True) if price_element else None

        sold_element = item.select_one("span._1cEkb")
        sold = sold_element.get_text(strip=True) if sold_element else None

        reviews_element = item.select_one("span.qzqFw")
        reviews = reviews_element.get_text(strip=True) if reviews_element else None

        location_element = item.select_one("span.oa6ri")
        location = location_element.get_text(strip=True) if location_element else None

        products.append({
            "name": name,
            "price": price,
            "sold": sold,
            "reviews": reviews,
            "location": location,
            "link": link,
        })

    return products
