from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stories/$', views.story_list, name='story_list'),
    url(r'^stories/(?P<id>\d+)/$', views.story_detail, name='story_detail'),

    url(r'^events/$', views.event_list, name='event_list'),
    url(r'^events/(?P<id>\d+)/$', views.event_detail, name='event_detail'),

    url(r'^tracks/$', views.track_list, name='track_list'),
    url(r'^tracks/new/$', views.track_new, name='track_new'),
    url(r'^tracks/(?P<id>\d+)/edit/$', views.track_edit, name='track_edit'),
    url(r'^tracks/(?P<id>\d+)/delete/$', views.track_delete, name='track_delete'),

    url(r'^regions/$', views.region_list, name='region_list'),
    url(r'^regions/(?P<id>\d+)/$', views.region_detail, name='region_detail'),

    url(r'^members/$', views.member_list, name='member_list'),
    url(r'^members/(?P<id>\d+)/$', views.member_detail, name='member_detail'),

    url(r'^/$', views.index, name='index'),
]
