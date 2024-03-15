from utils.redis_pool import POOL
import redis


def site_settings(request):
    conn = redis.StrictRedis(connection_pool=POOL)

    prefix = ''
    if hasattr(request, 'prefix'):
        prefix = request.prefix
    utils_s = {
        'site_title': '%s%s' % (prefix, conn.get('site_title')),
        'phone_number': conn.get('phone_number'),
        'company_address': conn.get('company_address'),
        'mail': conn.get('mail')
    }

    return {'site_settings': utils_s}
