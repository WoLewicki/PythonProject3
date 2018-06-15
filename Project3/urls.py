"""Project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from StackLike import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('home/new_question/', views.new_question, name='new_question'),
    path('home/add_question/', views.add_question, name='add_question'),
    re_path('home/new_response/(\\d+)/?$', views.new_response, name='new_response'),
    re_path('home/add_response/(\\d+)/?$', views.add_response, name='add_response'),
    re_path('home/([^/]+)/?$', views.category_page, name='category'),
    re_path('home/([^/]+)/(\\d+)/?$', views.show_question, name='show_question'),
    re_path('home/([^/]+)/(\\d+)/(\\d+)/([+-])$', views.vote, name='vote'),
]

