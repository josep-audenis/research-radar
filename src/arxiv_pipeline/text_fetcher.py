import requests
from bs4 import BeautifulSoup

class TextFetcher:  # Some papers do not have html...

    BASE_URL = "https://arxiv.org/html/"

    def get_full_text(self, arxiv_id):
        url =  f"{self.BASE_URL}{arxiv_id}"
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        body = soup.find("article")
        if not body:
            return None
        
        return body.get_text(separator="\n")