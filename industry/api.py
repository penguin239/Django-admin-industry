from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import JsonResponse
from industry.models import Product
from utils.redis_pool import POOL

import redis


def TopNProducts(request):
    data = []
    for item in Product.objects.all()[::-1][:8]:
        data.append(
            {
                'id': item.id,
                'name': item.name
            }
        )
    return JsonResponse(
        {
            'status_code': 200,
            'products': data
        }
    )


@staff_member_required
def set_site_setting(request):
    if request.method == 'POST':
        conn = redis.StrictRedis(connection_pool=POOL)
        phone = request.POST.get('site-phone')
        title = request.POST.get('site-title')
        site_email = request.POST.get('site-email')
        company_address = request.POST.get('company-address')

        conn.mset({
            'phone_number': phone,
            'site_title': title,
            'mail': site_email,
            'company_address': company_address
        })

        return JsonResponse({'status_code': 200})
    return JsonResponse({'status_code': 500})


@staff_member_required
def set_slogan(request):
    print(request.POST)
    slogan1 = request.POST.get('slogan1', None)
    slogan2 = request.POST.get('slogan2', None)
    intro = request.POST.get('intro', None)

    if slogan1 and slogan2:
        conn = redis.StrictRedis(connection_pool=POOL)
        conn.hset('HOME_PAGE:slogan:1', 'slogan', slogan1)
        conn.hset('HOME_PAGE:slogan:2', 'slogan', slogan2)
        conn.set('intro', intro)

        return JsonResponse({'status_code': 200})
    return JsonResponse({'status_code': 500})


@staff_member_required
def get_server_source(request):
    # 获取redis中存的服务器资源，供前端可视化
    conn = redis.StrictRedis(connection_pool=POOL)
    result = conn.lrange('server_resource', 0, -1)

    return JsonResponse(
        {
            'status_code': 200,
            'server_resource': result
        }
    )
