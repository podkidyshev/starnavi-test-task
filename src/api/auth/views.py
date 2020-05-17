from rest_framework_simplejwt.views import (
    TokenObtainPairView as SimpleJWTTokenObtainPairView,
    TokenRefreshView as SimpleJWTTokenRefreshView
)

from .serializers import TokenObtainPairSerializer


class TokenObtainPairView(SimpleJWTTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


# for consistency in urls.py
class TokenRefreshView(SimpleJWTTokenRefreshView):
    pass
