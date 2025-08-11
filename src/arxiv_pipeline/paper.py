class Paper:
    def __init__(self, title, authors, link, summary, published, categories, is_new):
        self.title = title
        self.authors = authors
        self.link = link
        self.summary = summary
        self.published  = published
        self.categories = categories
        self.is_new = is_new

    def to_dict(self):
        return {
            "title": self.title,
            "autor/s": self.authors,
            "link": self.link,
            "summary": self.summary,
            "published": self.published,
            "categories": self.categories,
            "is_new": self.is_new
        }