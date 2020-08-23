import requests
import pandas as pd
from bs4 import BeautifulSoup


def wiki_page(page):
    return f"https://stardewvalleywiki.com/{page}"


def get_page_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup


if __name__ == "__main__":
    pass
