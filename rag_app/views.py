from django.shortcuts import render
from rest_framework import status,viewsets,generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Interaction
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    pass

class TokenRefreshView(TokenRefreshView):
    pass

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]


class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all() 
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated]


class InteractionsByChatView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, chat_id):
        try:
            # Retrieve all interactions for the given chat_id
            interactions = Interaction.objects.filter(chat_id=chat_id)
            if not interactions.exists():
                return Response({"error": "No interactions found for the given chat_id"}, status=status.HTTP_404_NOT_FOUND)
            
            # Serialize the interactions
            serializer = InteractionSerializer(interactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginHistoryViewSet(viewsets.ModelViewSet):
    queryset = LoginHistory.objects.all()
    serializer_class = LoginHistorySerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class UserDetailsView(APIView):
    """
    View to get details of the currently authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # Get the authenticated user
        serializer = UserSerializer(user)  # Serialize the user object
        return Response(serializer.data)