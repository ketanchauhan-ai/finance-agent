import feedparser

def get_company_news(company):

    query = company.replace(" ", "+")

    url = f"https://news.google.com/rss/search?q={query}"

    feed = feedparser.parse(url)

    news = []

    for entry in feed.entries[:5]:
        news.append(entry.title)

    return news