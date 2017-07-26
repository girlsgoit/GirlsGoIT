from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stories/$', views.stories_list, name='stories_list')
    url(r'^stories/(?P<id>\d+)$', views.stories_detail, name='stories_detail')
]
