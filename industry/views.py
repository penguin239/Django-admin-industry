from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import TemplateResponse
from utils.redis_pool import POOL

import redis


# 后台用法
@staff_member_required
def site_manage(request):
    conn = redis.StrictRedis(connection_pool=POOL)

    back_data = {
        'slogan1': conn.hget('HOME_PAGE:slogan:1', 'slogan'),
        'slogan2': conn.hget('HOME_PAGE:slogan:2', 'slogan')
    }
    return TemplateResponse(
        request, 'admin/site-manage.html', back_data
    )
