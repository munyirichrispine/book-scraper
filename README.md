# Book Scraper

A Python web scraper that collects data on 1,000 books from books.toscrape.com, a practice site built for learning web scraping, and saves it to a CSV file.

## What it does
- Visits all 50 pages of the catalogue
- Extracts each book's title, price and star rating
- Pauses half a second between requests so it does not overload the server
- Handles failed pages without crashing, and reports which page failed
- Saves everything to books.csv

## Results
1,000 books collected in a single run. A sample of the output is included in books.csv.

## How to run
1. Install Python 3
2. Install the libraries:
   pip install requests beautifulsoup4
3. Run the program:
   python scraper.py

## Tools used
Python, requests, BeautifulSoup, csv
