import redis
from indexing.tokenizer import tokenize

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def search(query):
    tokens = tokenize(query)
    results = {}
    for token in tokens:
        docs = redis_client.zrevrange(f'inverted_index:{token}', 0, -1, withscores=True)
        for doc, score in docs:
            doc = doc.decode('utf-8')
            results[doc] = results.get(doc, 0) + score
    return sorted(results.items(), key=lambda x: x[1], reverse=True)
