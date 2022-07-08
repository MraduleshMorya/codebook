from django.urls import path

from asgi_channel_test import views

urlpatterns = [
    path('', views.index, name='chat_index'),
    path('<str:room_name>/', views.room, name='room'),
]