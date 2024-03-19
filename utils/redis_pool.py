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
