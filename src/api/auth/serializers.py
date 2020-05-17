from django.utils import timezone

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as SimpleJWTTokenObtainPairSerializer


class TokenObtainPairSerializer(SimpleJWTTokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)

        self.user.last_login = timezone.now()
        self.user.save()

        return attrs
