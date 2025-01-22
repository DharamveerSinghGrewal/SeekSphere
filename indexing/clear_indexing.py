import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Clear the entire database
def clear_database():
    redis_client.flushdb()
    print("Redis database has been cleared.")

if __name__ == "__main__":
    clear_database()
