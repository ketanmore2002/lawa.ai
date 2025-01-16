from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyTokenObtainPairView, TokenRefreshView, InteractionsByChatView, UserViewSet, UserDetailsView

# Create a router and register the UserViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # JWT Token endpoints
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Interactions by chat ID
    path('api/chats/<uuid:chat_id>/interactions/', InteractionsByChatView.as_view(), name='interactions_by_chat'),
    
    # Include the router URLs for the UserViewSet
    path('api/', include(router.urls)),


    path('api/user/', UserDetailsView.as_view(), name='user_details'),
]