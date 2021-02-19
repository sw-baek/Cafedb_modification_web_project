"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.index, name='home'), # 지도
    path('', views.home, name='home'), # 로그인 둘다 홈으로 .
    # url(r'^$', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),

    path('kakao/', include('kakao.urls')),
    path('edit/', include('edit.urls')),
    path('users/', include('users.urls')),
    path('bbs/', include('bbs.urls')),

]
