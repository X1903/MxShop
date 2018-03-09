"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
# from goods.views_base import GoodsListView

from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 调试登录
    url(r'^api-auth/', include('rest_framework.urls')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    url(r'goods/$', GoodsListView.as_view(), name='goods-list'),

    url(r'docs/$', include_docs_urls(title='慕雪生鲜')),

]
