from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView
)
from rest_framework.permissions import AllowAny

from .models import Message
from .serializers import MessageSerializer
from .paginations import MessagesPageNumberPagination


class MessageListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessagesPageNumberPagination


class MessageCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MessageRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
