from django.conf.urls import url

from . import views
# TEMPLATE TAGGING
app_name = 'basic_app'  # doit match dand le {} html pour appeler le url voulu

urlpatterns=[
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]