from django.shortcuts import render, HttpResponse
from industry.models import Category, Product
from urllib import parse

import base64


def url_decode(keyword):
    decode_base64_keyword = base64.b64decode(keyword).decode('utf-8')

    return parse.unquote(decode_base64_keyword)


def index(request):
    return render(
        request, 'index.html'
    )


def aboutUs(request):
    request.prefix = '关于我们-'
    return render(
        request, 'about-us.html', {
            'page_title': 'About Us',
            'site_location': '关于我们'
        }
    )


def products(request):
    request.prefix = '产品首页-'

    keyword = request.GET.get('category', None)
    result_product_list = []
    if keyword:
        category = url_decode(keyword)
        result_product_list = Product.objects.filter(category=category)
    else:
        # 访问默认加载第一个类别
        category_table = Category.objects.first()
        if category_table:
            result_product_list = Product.objects.filter(category=category_table.category)

    all_categories = Category.objects.filter(is_active=True)

    return render(
        request, 'products.html', {
            'page_title': 'Products Center',
            'site_location': '产品首页',
            'all_categories': all_categories,
            'result_product_list': result_product_list
        }
    )


def news(request):
    return render(
        request, 'news.html'
    )


def contactUs(request):
    return render(
        request, 'contact-us.html'
    )
