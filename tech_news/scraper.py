import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    # URL_BASE = 'https://blog.betrybe.com/'
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        response.raise_for_status()
    except (requests.Timeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    list_news = selector.css(".cs-overlay-link::attr(href)").getall()
    return list_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css("a.next::attr(href)").get()

    if not next_page_url:
        return None
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
