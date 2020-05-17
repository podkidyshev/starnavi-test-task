from django.urls import path

from rest_framework.routers import DefaultRouter

from .auth.views import TokenObtainPairView, TokenRefreshView
from .user.views import UserViewSet
from .user.routers import UserRouter
from .post.views import PostsViewSet
from .analytics.views import LikesAnalyticsView, UserAnalyticsView

user_router = UserRouter(trailing_slash=False)
user_router.register('user', UserViewSet, basename='user')

router = DefaultRouter(trailing_slash=False)
router.register('posts', PostsViewSet, basename='posts')

urlpatterns = [
    path('auth/obtain', TokenObtainPairView.as_view(), name='auth-obtain'),
    path('auth/refresh', TokenRefreshView.as_view(), name='auth-refresh'),

    path('analytics/', LikesAnalyticsView.as_view(), name='analytics'),
    path('analytics/user/<int:pk>', UserAnalyticsView.as_view(), name='analytics-user'),
]

urlpatterns += user_router.urls + router.urls
