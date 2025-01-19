import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
redis_client.set('test_key', 'test_value')
value = redis_client.get('test_key')
print(f"Value from Redis: {value.decode('utf-8')}")
