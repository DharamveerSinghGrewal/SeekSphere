import os
import requests
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from indexing.tokenizer import tokenize
from indexing.indexer import index_articles
from search_app.fetcher import fetch_and_save_articles
import redis
DATA_DIR = "./data"
TECHNOLOGY_KEYWORDS = [
    "artificial intelligence",
    "machine learning",
    "blockchain",
    "programming languages",
    "cybersecurity",
    "cloud computing",
    "data science",
    "robotics",
    "quantum computing",
    "software engineering",
]

if __name__ == "__main__":
    for keyword in TECHNOLOGY_KEYWORDS:
        print(f"Fetching articles for keyword: {keyword}")
        fetch_and_save_articles(keyword, max_articles=20)
    print("Indexing articles...")
    index_articles()
    print("Preloading and indexing completed.")
