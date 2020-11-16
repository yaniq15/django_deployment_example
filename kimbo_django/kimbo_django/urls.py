"""kimbo_django URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from kimbo_app import views
from help_app import views as views_help


urlpatterns = [
    url(r'^$', views_help.index, name='index'),
    url(r'^helpme/', include('help_app.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^kimbo_app/', include('kimbo_app.urls')),


    path('admin/', admin.site.urls),
]
