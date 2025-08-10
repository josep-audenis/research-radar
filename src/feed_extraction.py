import feedparser

FEED_URL = "https://arxiv.org/rss/cs.LG"


def extract_feed():
    
    feed = feedparser.parse(FEED_URL)
    print(feed)

if __name__ == "__main__.py":
    extract_feed()