import feedparser

FEED_URL = "https://arxiv.org/rss/cs.LG"

feed = feedparser.parse(FEED_URL)
print(feed)