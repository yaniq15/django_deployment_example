from django.conf.urls import url

from chrsikimb_app import views

urlpatterns = [
    url(r'^$', views.users, name='users')
]
