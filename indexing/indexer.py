import os
import redis
from indexing.tokenizer import tokenize

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def build_index(data_folder):
    for filename in os.listdir(data_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(data_folder, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                index_file(content, filename)

def update_inverted_index(data_folder):
    build_index(data_folder)

def index_file(content, filename):
    tokens = tokenize(content)
    for token in tokens:
        redis_client.zincrby(f'inverted_index:{token}', 1, filename)

