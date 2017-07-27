from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stories/$', views.story_list, name='story_list'),
    url(r'^stories/new/$', views.story_new, name='story_new'),
    url(r'^stories/(?P<id>\d+)/edit/$', views.story_edit, name='story_edit'),
    url(r'^stories/(?P<id>\d+)/delete/$', views.story_delete, name='story_delete'),

    url(r'^events/$', views.event_list, name='event_list'),
    url(r'^events/new/$', views.event_new, name='event_new'),
    url(r'^events/(?P<id>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^events/(?P<id>\d+)/delete/$', views.event_delete, name='event_delete'),

    url(r'^tracks/$', views.track_list, name='track_list'),
    url(r'^tracks/new/$', views.track_new, name='track_new'),
    url(r'^tracks/(?P<id>\d+)/edit/$', views.track_edit, name='track_edit'),
    url(r'^tracks/(?P<id>\d+)/delete/$', views.track_delete, name='track_delete'),

    url(r'^regions/$', views.region_list, name='region_list'),
    url(r'^regions/(?P<id>\d+)/edit/$', views.region_detail, name='region_detail'),
    url(r'^regions/new/$', views.region_new, name='region_new'),    
    url(r'^regions/(?P<id>\d+)/edit/$', views.region_edit, name='region_edit'),
    url(r'^regions/(?P<id>\d+)/delete/$', views.region_delete, name='region_delete'),

    url(r'^members/$', views.member_list, name='member_list'),
    url(r'^members/new/$', views.member_new, name='member_new'),
    url(r'^members/(?P<id>\d+)/edit/$', views.member_edit, name='member_edit'),
    url(r'^members/(?P<id>\d+)/delete/$', views.member_delete, name='member_delete'),

    url(r'^/$', views.index, name='index'),
]
