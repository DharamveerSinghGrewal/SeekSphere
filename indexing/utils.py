def get_snippet(filepath):
    """
    Extract the snippet (first line) from a file.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        snippet = f.readline().strip()
    return snippet
