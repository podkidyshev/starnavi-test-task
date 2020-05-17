from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import UserSerializer, UserSignupSerializer
from .permissions import UserAuthenticated


class UserViewSet(ViewSet):
    permission_classes = [UserAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        return Response(UserSerializer(instance=request.user).data)

    @action(detail=False, methods=['POST'])
    def signup(self, request, *args, **kwargs):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(True)
        user = serializer.save()
        return Response(UserSerializer(instance=user).data)
