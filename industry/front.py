from django.shortcuts import render, HttpResponse


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
    return render(
        request, 'products.html', {
            'page_title': 'Products Center',
            'site_location': '产品首页'
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
