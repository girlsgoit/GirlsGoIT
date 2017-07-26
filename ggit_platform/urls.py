from django.conf.urls import url
from . import views

urlpatterns = [
    url (r'^events$', views.event_list, name='event_list' ),
]
