from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stories/$', views.stories_list, name='stories_list'),
    url(r'^stories/(?P<id>\d+)$', views.stories_detail, name='stories_detail'),
    url(r'^events$', views.event_list, name='event_list'),
    url(r'^tracks/$', views.track_list, name='track_list'),
    url(r'^tracks/(?P<id>\d+)$', views.track_detail, name='track_detail'),
    url(r'^tracks/$', views.track_list, name='track_list'),
    url(r'^track_detail/(?P<id>\d+)$', views.track_detail, name='track_detail'),
    url(r'^regions/$', views.region_list, name='region_list'),
    url(r'^members/$', views.member_list, name='member_list'),
    url(r'^members/(?P<id>\d+)$', views.member_detail, name='member_detail'),
    url(r'^$', views.index, name='index'),
]
