# pylint: skip-file
from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_page, name='login_page')
]
