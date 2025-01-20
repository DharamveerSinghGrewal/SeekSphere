from django.shortcuts import render
from .fetcher import fetch_articles
from indexing.query import search
from indexing.indexer import update_inverted_index

def index(request):
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        if not query:
            return render(request, 'search_app/index.html', {'error': 'Please enter a valid query.'})
        
        results = search(query)

        if len(results) < 5:
            fetch_articles(query, max_articles=5)
            update_inverted_index('./data')
            results = search(query)
        
        return render(request, 'search_app/index.html', {'results': results, 'query': query})
    
    return render(request, 'search_app/index.html')


