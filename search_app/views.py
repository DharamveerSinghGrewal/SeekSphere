from django.shortcuts import render

from indexing.query import search

def index(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        results = search(query)
        return render(request, 'search_app/index.html', {'results': results, 'query': query})
    return render(request, 'search_app/index.html')
