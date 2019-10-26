from django.urls import path

from .views import MessageCreateAPIView, MessageListAPIView, MessageRetrieveAPIView


urlpatterns = [
    path('create/', MessageCreateAPIView.as_view(), name='create_message_url'),
    path('list/', MessageListAPIView.as_view(), name='list_messages_url'),
    path('single/<int:pk>/', MessageRetrieveAPIView.as_view(), name='single_message_url')
]
