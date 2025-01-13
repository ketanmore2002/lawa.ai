from rest_framework import serializers
from .models import *


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'


class LoginHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginHistory
        fields = '__all__'