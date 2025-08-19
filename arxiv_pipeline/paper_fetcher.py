import json
import feedparser

from arxiv_pipeline.paper import Paper

class PaperFetcher:
    BASE_URL = "https://arxiv.org/rss/"

    def __init__(self, preference_file):
        with open(preference_file, "r") as f:
            self.preferences = json.load(f)
            self.url = self.BASE_URL
            self.n_fields = 0

    def fetch_papers(self):

        for field, field_data in self.preferences.items():
            
            if field_data["active"]:
                if self.n_fields > 0:
                    self.url += "+"
                self.url += f"{field}"
                self.n_fields += 1
                continue

            for sub, sub_data in field_data.get("subfields", {}).items():
                if sub_data["active"]:
                    if self.n_fields > 0:
                        self.url += "+"
                    self.url +=  f"{field}.{sub}"
                    self.n_fields += 1
        
        return self.fetch_feed()
        
    def fetch_feed(self):

        feed = feedparser.parse(self.url)
        papers = []
        for entry  in feed.entries:

            categories = []
            for tag in entry.tags:
                categories.append(tag["term"])

            papers.append(Paper(
                title = entry.title,
                authors = entry.author,
                link = entry.link,
                abstract = entry.summary.split("Abstract: ")[1],
                published = entry.published,
                categories = categories,
                is_new = True if entry.arxiv_announce_type == "new" else False
            ))

        return papers