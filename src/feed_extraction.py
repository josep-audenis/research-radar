import feedparser

FEED_URL = "https://arxiv.org/rss/cs.LG"


def extract_feed():
    
    feed = feedparser.parse(FEED_URL)
    print("feed:")
    #print(feed)
    
    for entry in feed.entries:
        print(entry.title)
        print(entry.link)
        print(entry.category)
        for tag in entry.tags:
            print(tag["term"])

if __name__ == "__main__":
    extract_feed()


    #'tags': [{'term': 'cs.LG', 'scheme': None, 'label': None}, {'term': 'stat.ME', 'scheme': None, 'label': None}, {'term': 'stat.ML', 'scheme': None, 'label': None}]