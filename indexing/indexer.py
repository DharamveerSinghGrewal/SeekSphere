import redis
from indexing.tokenizer import tokenize
import os

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def build_index(data_folder):
    for filename in os.listdir(data_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(data_folder, filename), 'r') as file:
                content = file.read()
                tokens = tokenize(content)
                doc_id = filename
                for token in tokens:
                    redis_client.zincrby(f'inverted_index:{token}', 1, doc_id)
