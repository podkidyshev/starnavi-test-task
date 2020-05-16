from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import UserSerializer


class UserViewSet(ViewSet):
    def retrieve(self, request, *args, **kwargs):
        return Response(UserSerializer(instance=request.user).data)

    @action(detail=False, methods=['POST'])
    def signup(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def login(self, request, *args, **kwargs):
        pass

    @action(detail=False, methods=['POST'])
    def refresh(self, request, *args, **kwargs):
        pass
