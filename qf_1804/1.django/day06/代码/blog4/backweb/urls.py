
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from backweb import views

urlpatterns = [
    # django自带登录注销
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    # url(r'index/', login_required(views.index), name='index'),
    # url(r'addArt/', login_required(views.addArt), name='add_art'),

    # 自己实现登录注册注销
    url(r'^my_register/', views.my_register, name='my_register'),
    url(r'^my_login/', views.my_login, name='my_login'),
    # url(r'my_logout/', views.my_logout, name='my_logout'),

    url(r'index/', views.index, name='index'),
    url(r'addArt/', views.addArt, name='add_art'),
]