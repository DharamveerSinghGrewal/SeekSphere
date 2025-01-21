from django.shortcuts import render
from .fetcher import fetch_articles
from indexing.query import search
from indexing.indexer import update_inverted_index

import os

def index(request):
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        
        # Handle empty query case
        if not query:
            return render(request, 'search_app/index.html', {
                'error': 'Please enter a valid query.'
            })
        
        # Search in the index
        results = search(query)

        # If fewer than 5 results are found, fetch and re-index
        if len(results) < 5:
            fetch_articles(query, max_articles=5)
            update_inverted_index('./data')
            results = search(query)

        # Enhance results with snippets
        refined_results = []
        for doc_id, score in results:
            filepath = os.path.join('./data', doc_id)
            snippet = extract_snippet(filepath)
            refined_results.append({
                'title': doc_id.replace('_', ' ').replace('.txt', ''),
                'score': score,
                'snippet': snippet,
            })

        return render(request, 'search_app/index.html', {
            'results': refined_results,
            'query': query
        })

    return render(request, 'search_app/index.html')


def extract_snippet(filepath):
    """
    Reads the first line from a file to use as a snippet.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.readline().strip()
    except FileNotFoundError:
        return "Snippet not available."
    except Exception as e:
        return f"Error reading snippet: {str(e)}"



