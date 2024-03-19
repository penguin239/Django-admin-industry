from django.http.response import JsonResponse
from industry.models import Product


def ServerSituation(request):
    return JsonResponse(
        {
            'status_code': 200,
            'status': 'success'
        }
    )


def TopNProducts(request):
    data = []
    for item in Product.objects.all()[:8]:
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
