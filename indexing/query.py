import redis
from indexing.tokenizer import tokenize

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def search(query):
    tokens = tokenize(query)
    results = {}

    for token in tokens:
        docs = redis_client.zrevrange(f'inverted_index:{token}', 0, -1, withscores=True)
        for doc, score in docs:
            doc_id = doc.decode('utf-8')
            results[doc_id] = results.get(doc_id, 0) + score
     # Boost for documents matching all tokens
    for doc_id in results.keys():
        if all(token in doc_id.lower() for token in tokens):
            results[doc_id] *= 2
    
    # Sort results by score in descending order
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    # Apply a dynamic score threshold
    if sorted_results:
        top_score = sorted_results[0][1]
        threshold = top_score * 0.1  # Keep results with at least 10% of the top score
        print(f"Top score: {top_score}, Threshold: {threshold}")  # Debugging threshold
        filtered_results = [result for result in sorted_results if result[1] >= threshold]
    else:
        filtered_results = []

    return filtered_results

