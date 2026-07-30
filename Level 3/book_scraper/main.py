import os
import csv
import requests
from bs4 import BeautifulSoup
BASE_URL = "https://books.toscrape.com/"
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books.csv")
def display_title():
    print("\n========================")
    print("      BOOK SCRAPER")
    print("========================")
    print(f"Target: {BASE_URL}")
def save_to_csv(books, path):
    with open(path, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["title","price","rating","availability"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    book_elements = soup.find_all("article",class_="product_pod")
    books = []
    for element in book_elements:
        title = element.find("h3").find("a")["title"]
        price = element.find("p",class_="price_color").text.strip()
        rating = element.find("p",class_="star-rating")["class"][1]
        availability = element.find("p",class_="instock availability").text.strip()
        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
        })
    return books
def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        print(f"Could not fetch the page: {error}")
        return None
def display_books(books):
    print(f"\nFound {len(books)} books:\n")
    for book in books:
        title = book["title"]
        print(f"  {title} ............................... {book['price']}  "f"({book['rating']} stars, {book['availability']})")
def main():
    display_title()
    print(f"\nFetching page...")
    html = fetch_page(BASE_URL)
    if not html: return
    print("Parsing books...")
    books = parse_books(html)
    if not books:
        print("No books found the page structure may have changed.")
        return
    display_books(books)
    save_to_csv(books,CSV_PATH)
    print("\n========================")
    print(f"Saved {len(books)} books to books.csv")
    print("========================")
if __name__ == "__main__":
    main()
