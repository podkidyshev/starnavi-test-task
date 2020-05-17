from django.utils import timezone

from rest_framework_simplejwt.authentication import JWTAuthentication as SimpleJWTAuthentication

from starnavi.user.models import User


class JWTAuthentication(SimpleJWTAuthentication):
    def authenticate(self, request):
        user, token = super().authenticate(request)

        if isinstance(user, User):
            user.last_request = timezone.now()
            user.save(update_fields=['last_request'])

        return user, token
