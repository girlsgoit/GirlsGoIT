from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^events$', views.event_list, name='event_list' ),
    url(r'^tracks/$', views.tracks_list, name='tracks_list'),
    url(r'^track_detail/(?P<id>\d+)$', views.track_detail, name='track_detail'),
    url(r'^regions/$', views.region_list, name='regions_list'),
    url(r'^members/$', views.member_list, name='members_list'),
]

