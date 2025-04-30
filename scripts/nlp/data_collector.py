import requests
from bs4 import BeautifulSoup
import snscrape.modules.twitter as sntwitter

def collect_articles(urls):
    articles = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join(p.text for p in paragraphs)
            articles.append(text)
        except Exception as e:
            print(f"Error collecting data from {url}: {e}")
    return articles

def collect_tweets(query, max_results=100):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) >= max_results:
            break
        tweets.append(tweet.content)
    return tweets
