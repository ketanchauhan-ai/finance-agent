# news_data.py

import feedparser

def get_company_news(company):
    query = company.replace(" ", "+")

    feed_url = f"https://news.google.com/rss/search?q={query}"

    feed = feedparser.parse(feed_url)

    headlines = []

    for entry in feed.entries[:5]:
        headlines.append(entry.title)

    return headlines