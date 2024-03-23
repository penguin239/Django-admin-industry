"""
URL configuration for django_simple project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from industry import views, front
from industry import api

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    path('site-manage/', views.site_manage, name='site-manage'),

    # static
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # api
    path('api/ServerSituation/', api.ServerSituation, name='ServerSituation'),
    path('api/TopNProducts/', api.TopNProducts, name='topNProducts'),
    path('api/set-setting/', api.set_site_setting, name='set-setting'),
    path('api/set-slogan/', api.set_slogan, name='set-slogan'),
    path('api/get-server-resource/', api.get_server_source, name='get-server-resource'),

    # front
    path('', front.index, name='index'),
    path('about-us/', front.aboutUs, name='aboutUs'),
    path('products/', front.products, name='products'),
    path('contact-us/', front.contactUs, name='contact-us'),
    path('product-detail/', front.productDetail, name='product-detail'),
    path('leave-message/', front.leaveMessage, name='leave-message')
]
