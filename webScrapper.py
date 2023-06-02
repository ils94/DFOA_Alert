from bs4 import BeautifulSoup
import requests


def bs4soup(link):
    referer = "https://www.google.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/108.0.0.0 Safari/537.36", "referer": referer}

    return BeautifulSoup(requests.get(link, headers=headers).text, 'html.parser')
