from django.http.response import JsonResponse


def ServerSituation(request):
    return JsonResponse({'status': 'success'})
