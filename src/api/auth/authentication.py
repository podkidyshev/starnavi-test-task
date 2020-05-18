from django.utils import timezone

from rest_framework_simplejwt.authentication import JWTAuthentication as SimpleJWTAuthentication

from starnavi.user.models import User


class JWTAuthentication(SimpleJWTAuthentication):
    def authenticate(self, request):
        auth_result = super().authenticate(request)

        if isinstance(auth_result, tuple) and isinstance(auth_result[0], User):
            auth_result[0].last_request = timezone.now()
            auth_result[0].save(update_fields=['last_request'])

        return auth_result
