def get_snippet(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        snippet = f.readline().strip()  # Read the first line as the snippet
    return snippet
