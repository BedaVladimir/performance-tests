from redis import Redis

cache = Redis(host='redis', port=6379)
cache.incr("times", 1)
print(cache.get("times"))