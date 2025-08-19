class Paper:
    def __init__(self, title, authors, link, abstract, published, categories, is_new):
        self.title = title
        self.authors = authors
        self.link = link
        self.abstract = abstract
        self.published  = published
        self.categories = categories
        self.is_new = is_new

    def matches_keywords(self, keywords):
        text = f"{self.title} {self.abstract}".lower()
        return any(f" {keyword.lower()} " in text for keyword in keywords)

    def to_dict(self):
        return {
            "title": self.title,
            "autor/s": self.authors,
            "link": self.link,
            "abstract": self.abstract,
            "published": self.published,
            "categories": self.categories,
            "is_new": self.is_new
        }