from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.detail, name='main'),
    url(r'^db', views.db, name='db')
]
