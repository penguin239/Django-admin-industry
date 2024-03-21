from django.http import JsonResponse
from django.shortcuts import render
from industry.models import Category, Product, LeaveMessage
from django_simple import settings
from urllib import parse
from utils.redis_pool import POOL

import requests
import base64
import redis


def __get_location(ip_addr):
    response = requests.get(f'https://whois.pconline.com.cn/ipJson.jsp?ip={ip_addr}&json=true', timeout=3)
    if response.status_code == 200:
        return response.json().get('addr', 'Unknown')
    return 'Unknown'


def url_decode(keyword):
    decode_base64_keyword = base64.b64decode(keyword).decode('utf-8')

    return parse.unquote(decode_base64_keyword)


def url_encode(keyword):
    unquote_keyword = parse.quote(keyword)

    return base64.b64encode(unquote_keyword.encode()).decode('utf-8')


def index(request):
    all_product = Product.objects.all()
    conn = redis.StrictRedis(connection_pool=POOL)

    back_data = {
        'slogan1': conn.hget('HOME_PAGE:slogan:1', 'slogan'),
        'slogan2': conn.hget('HOME_PAGE:slogan:2', 'slogan')
    }

    return render(
        request, 'index.html',
        {
            'show_product': all_product[:8],
            'media_base_url': settings.MEDIA_URL,
            'back_data': back_data
        }
    )


def aboutUs(request):
    request.prefix = '关于我们-'
    return render(
        request, 'about-us.html', {
            'page_title': 'About Us',
            'site_location': '关于我们'
        }
    )


def products(request, is_extend=False):
    request.prefix = '产品首页-'

    keyword = request.GET.get('category', None)
    result_product_list = []
    category = ''

    if keyword:
        category = url_decode(keyword)
        category_id = Category.objects.filter(category=category).first()
        result_product_list = Product.objects.filter(category_id=category_id.id)
    else:
        # 访问默认加载第一个类别
        category_table = Category.objects.filter(is_active=True).first()
        if category_table:
            result_product_list = Product.objects.filter(category_id=category_table.id)
            category = category_table.category

    all_categories = Category.objects.filter(is_active=True)

    context = {
        'page_title': 'Products Center',
        'site_location': f'产品首页 > {category}',
        'all_categories': all_categories,
        'result_product_list': result_product_list,
        'label_highlight': category,
        'media_base_url': settings.MEDIA_URL,
    }

    if is_extend:
        return context
    return render(request, 'products.html', context)


def news(request):
    return render(
        request, 'news.html'
    )


def contactUs(request):
    return render(
        request, 'contact-us.html'
    )


def productDetail(request):
    product_id = request.GET.get('product-id', None)
    if not product_id:
        pass
    product = Product.objects.filter(id=product_id).first()
    category = Category.objects.filter(id=product.category_id).first()

    context = products(request, True)
    context['site_location'] += f' > {product.name}'
    context['label_highlight'] = category.category
    context['product'] = product
    context['belong_category'] = url_encode(category.category)

    context['param_img'] = settings.MEDIA_URL + str(product.param_image)

    del context['result_product_list']

    return render(
        request, 'product-detail.html', context
    )


def leaveMessage(request):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    phone = request.POST.get('phone', None)
    ip_addr = request.META.get('REMOTE_ADDR', None)
    user_location = __get_location(ip_addr)
    message = request.POST.get('message', None)

    save_leaveMsg = LeaveMessage.objects.create(
        name=name, email=email, phone=phone,
        ipAddr=ip_addr, place=user_location, message=message
    )
    save_leaveMsg.save()

    return JsonResponse({'status_code': 200})
