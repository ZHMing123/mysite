"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from mysite import views
"""写到views中
# from django.shortcuts import HttpResponse, render
# 
# 
# def zhming(request):
#     # request参数保存了所有和浏览器请求相关是数据
#     return HttpResponse('hello zhming!')
# 
# 
# def hello(request):
#     # request参数保存了所有和浏览器请求相关是数据
#     # 手动找HTML文件
#     # with open("templates/zhming.html", "r", encoding="utf-8") as f:
#     #     data = f.read()
#     # return HttpResponse(data)
# 
#     # Django找html文件
#     return render(request, "zhming.html")
# 
# def login(request):
#     return render(request, "login_demo.html")
"""

# 保存了路径和函数的对应关系
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^zhming/', views.zhming),
    url(r'^hello/', views.hello),
    url(r'^login/', views.login),
    url(r'^user_list/', views.user_list),
    url(r'^add_user/', views.add_user),
    url(r'^delete_user/', views.delete_user),
    url(r'^edit_user/', views.edit_user),
    url(r'^login_validate/', views.login_validate),

    # 出版社相关的对应关系
    url(r'^publisher_list/', views.publisher_list),
    url(r'^add_publisher/', views.add_publisher),
    url(r'^delete_publisher/', views.delete_publisher),
    url(r'^edit_publisher/', views.edit_publisher),

    # 书相关的对应关系
    url(r'^book_list/', views.book_list),
    url(r'^add_book/', views.add_book),
    url(r'^delete_book/', views.delete_book),
    url(r'^edit_book/', views.edit_book),

    # 作者相关的对应关系
    url(r'^author_list/', views.author_list),
    url(r'^add_author/', views.add_author),
    url(r'^delete_author/', views.delete_author),
    url(r'^edit_author/', views.edit_author),


]
