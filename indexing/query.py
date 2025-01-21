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
    
    # Sort results by score in descending order
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    # Apply a score threshold: retain results with at least 10% of the top score
    if sorted_results:
        threshold = sorted_results[0][1] * 0.1
        sorted_results = [result for result in sorted_results if result[1] >= threshold]
    
    return sorted_results

