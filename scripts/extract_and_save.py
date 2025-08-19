import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from arxiv_pipeline.paper_fetcher import PaperFetcher
from arxiv_pipeline.paper_filter import PaperFilter
from arxiv_pipeline.paper_store import PaperStore

fetcher = PaperFetcher("data/feed_preference.json")
all_papers = fetcher.fetch_papers()

print(f"A total of {len(all_papers)} papers have been fetched. \nFiltering...")

filterer = PaperFilter(fetcher.preferences)
relevant_papers = filterer.filter(all_papers)

store = PaperStore("data/filtered_papers.json")
store.save(relevant_papers)

print(f"Saved {len(relevant_papers)} relevant papers.")