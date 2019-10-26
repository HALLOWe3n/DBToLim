from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True, max_length=254)

    class Meta:
        model = Message
        fields = [
            'id',
            'email',
            'message',
            'created',
            'updated'
        ]
