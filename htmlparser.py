import requests

product = phone

url = f"https://shopee.ph/search?keyword={product}"

response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    with open("page.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("HTML saved successfully!")
else:
    print("Failed to retrieve page")
