import redis
# pip install redis
# docker run --net=host redis

rc = redis.StrictRedis(host="localhost", port=6379, db=0)

print(rc.keys())
print(rc.set('k1', 'v1'))
print(rc.keys())
print(rc.get('k1'))
print(rc.incr('k2'))
print(rc.get('k2'))
print(rc.delete('k2'))
print(rc.get('k2'))
