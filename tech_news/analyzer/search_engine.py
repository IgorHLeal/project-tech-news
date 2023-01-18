from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news_list = search_news(query)
    news_tuple = []

    for new in news_list:
        new_search = (new['title'], new['url'])
        news_tuple.append(new_search)
    return news_tuple


# Requisito 7
def search_by_date(date):
    try:
        news_tuple = []
        news_by_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": {"$eq": news_by_date}}

        for new in search_news(query):
            search = (new['title'], new['url'])
            news_tuple.append(search)
        return news_tuple
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
