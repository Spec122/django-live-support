from django.urls import path, include
from live_support import views

urlpatterns = [
    path('^$', views.start_chat, name='start_chat'),
    path('^(?P<support_group_id>\d+)/$', views.start_chat, name='start_chat_for_group'),
    path('^ajax/get_messages/$', views.get_messages, name='get_messages'),
    path('^ajax/(?P<chat_id>\d+)/post_message/$', views.post_message, name='post_message'),
    path('^ajax/(?P<chat_id>\d+)/end_chat/$', views.end_chat, name='end_chat'),
    path('^ajax/(?P<chat_id>\d+)/join_chat/$', views.join_chat, name='join_chat'),
    path('^(?P<chat_uuid>[\w-]+)/end_chat/$', views.client_end_chat, name='client_end_chat'),
    path('^(?P<chat_uuid>[\w-]+)/get_messages/$', views.client_get_messages, name='client_get_messages'),
    path('^(?P<chat_uuid>[\w-]+)/post_message/$', views.client_post_message, name='client_post_message'),
    path('^(?P<chat_uuid>[\w-]+)/$', views.client_chat, name='client_chat'),
]

