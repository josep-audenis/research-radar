# Research Radar

Research Radar is a lightweight tool to fetch, filter, and track arXiv papers based on your research interests.

It let's you configure which arXiv categories you care about and which keywords matter to you.
Relevant papers are automatically stored in JSON for later browsing or integration into your workflow.

## Features

- Fetches papers directly from ArXiv RSS feeds
- Cateogry-based filtering (e.g., cs.AI, cs.LG, math.ST, ...)
- Keyword-based filtering (search in abstract)
- Stores matched papers in clean JSON format.
- EXtensible class-based architecture for future integration (email digests, web UI, etc.)

## Project Structure

```
├── arxiv_pipeline/
│   ├── __init__.py
│   ├── paper.py
│   ├── paper_fetcher.py
│   ├── paper_filter.py
│   └── paper_store.py
├── data/
│   └── feed_preference.json
├── scripts/
│   └── extract_and_save.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Preferences

Edit the ``data/feed_preference.json`` to choose your fields and keywords. The only fields that should be modified are the ``active`` to fetch papers from that category/subcategory, and the ``keywords`` to filter the fetched papers. Example:

```json
{
    "cs": {
        "name": "Computer Science",
        "active": false,
        "keywords": [],
        "subfields": {
            "ai": {
                "name": "Artificial Intelligence",
                "active": true,
                "keywords": ["transformer", "rag"]
            },
            "ar": {
                "name": "Hardware Architecture",
                "active": false,
                "keywords": []
            }
        }
    }
}
```

## Usage

1. Clone the repository:

```git
git clone https://github.com/josep-audenis/research-radar.git
cd research-radar
```

or 

```git
git clone git@github.com:josep-audenis/research-radar.git
cd research-radar
```

2. Create a virtual environment (Optional):

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python scripts/extract_and_save.py
```

5. View results in:

```bash
data/filtered_papers.json
```

## Upcoming Upgrades

- [ ] Email daily/weekly digest of filtered papers.
- [ ] Advanced filtering.
- [ ] Full paper keyword serach.