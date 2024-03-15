from django_simple import settings
import redis

REDIS_CONFIG = settings.REDIS_CONFIG

POOL = redis.ConnectionPool(
    host=REDIS_CONFIG['host'],
    port=REDIS_CONFIG['port'],
    db=REDIS_CONFIG['db'],
    password=REDIS_CONFIG['password'],
    decode_responses=True
)


if __name__ == '__main__':
    # todo 商品分类redis设计
    r = redis.StrictRedis(connection_pool=POOL)
    # r.hset('leibie:test1', 0, 'value1')
    print(r.hkeys('leibie'))
