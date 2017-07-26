from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^regions/$', views.region_list, name='regions_list'),
    url(r'^members/$', views.member_list, name='members_list'),
]
