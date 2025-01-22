from django.shortcuts import render
from indexing.query import search
from indexing.indexer import update_inverted_index
from indexing.tokenizer import tokenize
import re
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

        # Enhance results with snippets
        refined_results = []
        for doc_id, score in results:
            filepath = os.path.join('./data', doc_id)
            snippet = extract_snippet(filepath, query)
            article_url = f"https://en.wikipedia.org/wiki/{doc_id.replace('.txt', '').replace('_', '_')}"
            refined_results.append({
                'title': doc_id.replace('_', ' ').replace('.txt', ''),
                'score': score,
                'snippet': snippet,
                'url': article_url,
            })

        return render(request, 'search_app/index.html', {
            'results': refined_results,
            'query': query
        })

    return render(request, 'search_app/index.html')

def extract_snippet(filepath, query):
    """
    Reads the first line from a file and highlights query tokens in the snippet.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            snippet = f.readline().strip()
            return highlight_keywords(snippet, query)
    except FileNotFoundError:
        return "Snippet not available."
    except Exception as e:
        return f"Error reading snippet: {str(e)}"

def highlight_keywords(text, query):
    """
    Bold and italicize query keywords in the text.
    """
    tokens = tokenize(query)  # Use the same tokenize function for consistency
    for token in tokens:
        # Use regex for case-insensitive replacement
        text = re.sub(
            rf'\b({re.escape(token)})\b',  # Match whole words
            r'<b><i>\1</i></b>',          # Wrap in <b><i></i></b>
            text,
            flags=re.IGNORECASE           # Case-insensitive match
        )
    return text




