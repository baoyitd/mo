import redis
from util import dbconf
pool = redis.ConnectionPool(host=dbconf.REDIS_HOST, port=dbconf.REDIS_PORT, db=dbconf.REDIS_FLOWDB, password=dbconf.REDIS_PWD, decode_responses=True)

def getRedis():
    return redis.Redis(connection_pool=pool)
