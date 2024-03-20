from django.http.response import JsonResponse
from industry.models import Product

from utils.redis_pool import POOL


def ServerSituation(request):
    return JsonResponse(
        {
            'status_code': 200,
            'status': 'success'
        }
    )


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
