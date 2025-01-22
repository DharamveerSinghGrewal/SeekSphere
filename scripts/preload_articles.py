import os
import requests
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from indexing.tokenizer import tokenize
from indexing.indexer import index_file
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

def fetch_and_save_articles(keyword, max_articles=50):
    """
    Fetches articles related to a specific keyword and saves them to local files.
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": keyword,
        "format": "json",
        "srlimit": max_articles
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        results = response.json().get("query", {}).get("search", [])
        
        for result in results:
            title = result["title"]
            content = fetch_article_content(title)
            if content:
                save_article_to_file(title, content)
    except requests.RequestException as e:
        print(f"Error fetching articles for keyword '{keyword}': {e}")

def fetch_article_content(title):
    """
    Fetches the content of an article by title from Wikipedia.
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        pages = response.json().get("query", {}).get("pages", {})
        return next(iter(pages.values())).get("extract", "")
    except requests.RequestException as e:
        print(f"Error fetching article content for '{title}': {e}")
        return ""

def save_article_to_file(title, content):
    """
    Saves article content to a file for indexing.
    """
    safe_title = title.replace(" ", "_")
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, f"{safe_title}.txt")
    
    if not os.path.exists(filepath):  # Avoid overwriting
        snippet = content[:200].replace('\n', ' ') + "..."  # First 200 characters as snippet
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"{snippet}\n\n{content}")  # Save snippet at the top of the file

def index_articles():
    """
    Reads all articles in the data folder and indexes them.
    """
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.txt'):
            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                index_file(content, filename)

if __name__ == "__main__":
    """for keyword in TECHNOLOGY_KEYWORDS:
        print(f"Fetching articles for keyword: {keyword}")
        fetch_and_save_articles(keyword, max_articles=20)"""
    print("Indexing articles...")
    index_articles()
    print("Preloading and indexing completed.")
