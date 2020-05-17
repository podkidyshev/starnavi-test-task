from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .user.views import UserViewSet
from .user.routers import UserRouter

user_router = UserRouter()
user_router.register('user', UserViewSet, basename='user')

urlpatterns = user_router.urls + [
    path('auth/obtain', TokenObtainPairView.as_view(), name='auth-obtain'),
    path('auth/refresh', TokenRefreshView.as_view(), name='auth-refresh'),
]
