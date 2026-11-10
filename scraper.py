import csv
import time
import requests
from bs4 import BeautifulSoup

rating_words = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
books = []

for page in range(1, 51):
    URL = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Page {page} failed: {error}")
        continue

    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]
        price = float(item.select_one("p.price_color").text.replace("£", ""))
        rating = rating_words[item.select_one("p.star-rating")["class"][1]]
        books.append({"title": title, "price": price, "rating": rating})

    # Polite pause between requests to avoid hammering the server
    time.sleep(0.5)

print("Books found:", len(books))
for book in books[:3]:
    print(book)

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "rating"])
    writer.writeheader()
    writer.writerows(books)

print("Saved to books.csv")