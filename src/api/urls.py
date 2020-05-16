from .user.views import UserViewSet
from .user.routers import UserRouter

user_router = UserRouter()
user_router.register('user', UserViewSet, basename='user')

urlpatterns = user_router.urls + [

]
