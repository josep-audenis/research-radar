import sys
import os
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from arxiv_pipeline.paper_fetcher import PaperFetcher
from arxiv_pipeline.paper_filter import PaperFilter
from arxiv_pipeline.paper_store import PaperStore

fetcher = PaperFetcher("config/feed_preference.json")
all_papers = fetcher.fetch_papers()

print(f"A total of {len(all_papers)} papers have been fetched. \nFiltering...")

filterer = PaperFilter(fetcher.preferences)
relevant_papers = filterer.filter(all_papers)

date = datetime.datetime.now().strftime("%Y-%m-%d")

store = PaperStore(f"data/filtered_papers_{date}.json")
store.save(relevant_papers)

print(f"Saved {len(relevant_papers)} relevant papers.")