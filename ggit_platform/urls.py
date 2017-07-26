from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^tracks/$', views.tracks_list, name='tracks_list'),
    url(r'^track_detail/(?P<id>\d+)$', views.track_detail, name='track_detail')
]

