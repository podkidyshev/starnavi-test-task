from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .user.views import UserViewSet
from .user.routers import UserRouter
from .post.views import PostsViewSet
from .analytics.views import AnalyticsView

user_router = UserRouter(trailing_slash=False)
user_router.register('user', UserViewSet, basename='user')

router = DefaultRouter(trailing_slash=False)
router.register('posts', PostsViewSet, basename='posts')

urlpatterns = [
    path('auth/obtain', TokenObtainPairView.as_view(), name='auth-obtain'),
    path('auth/refresh', TokenRefreshView.as_view(), name='auth-refresh'),

    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]

urlpatterns += user_router.urls + router.urls
