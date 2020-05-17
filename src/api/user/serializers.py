from django.contrib.auth.hashers import make_password

from rest_framework.serializers import ModelSerializer, HiddenField

from starnavi.user.models import User


class UserSignupSerializer(ModelSerializer):
    is_staff = HiddenField(default=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, password):
        return make_password(password)


class UserSerializer(ModelSerializer):
    is_staff = HiddenField(default=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']
        read_only_fields = ['id']
