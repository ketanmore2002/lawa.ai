from django.shortcuts import render
from rest_framework import status,viewsets,generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    pass

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]


class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all() 
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated]


class LoginHistoryViewSet(viewsets.ModelViewSet):
    queryset = LoginHistory.objects.all()
    serializer_class = LoginHistorySerializer
    permission_classes = [IsAuthenticated]