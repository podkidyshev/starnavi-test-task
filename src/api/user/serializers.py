from rest_framework.serializers import ModelSerializer, HiddenField

from starnavi.user.models import User


class UserSerializer(ModelSerializer):
    is_staff = HiddenField(default=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']
        read_only_fields = ['id']
