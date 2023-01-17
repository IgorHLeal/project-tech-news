import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup

from tech_news.database import create_news


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
    selector = Selector(html_content)

    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".meta-author .author a::text").get(),
        "comments_count": selector.css(".comment-list li").getall() or 0,
        "summary": BeautifulSoup(
            selector.css(".entry-content p").get(), "html.parser"
        ).get_text().strip(),
        "tags": selector.css("a[rel=tag]::text").getall(),
        "category": selector.css(".label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    url_base = 'https://blog.betrybe.com/'
    list_news = []

    while len(list_news) <= amount:
        html_content = fetch(url_base)
        list_url_news = scrape_updates(html_content)

        for new_url in list_url_news:
            new_fetch_url = fetch(new_url)
            list_news.append(scrape_news(new_fetch_url))
        url_base = scrape_next_page_link(html_content)

    create_news(list_news[:amount])

    return list_news[:amount]
