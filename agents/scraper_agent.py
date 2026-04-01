import requests
from newspaper import Article

class ScraperAgent:
def __init__(self, api_key):
    self.api_key = api_key

def fetch_news(self, query="India"):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={self.api_key}&language=en"
    
    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])
    return articles[:5]

def get_full_article(self, url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return "Could not fetch article content"