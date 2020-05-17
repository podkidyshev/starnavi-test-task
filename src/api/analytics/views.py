from django.db.models import Count

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from starnavi.post.models import Like
from starnavi.user.models import User

from .serializers import LikesAnalyticsInputSerializer, LikesAnalyticsOutputSerializer, UserAnalyticsSerializer


class LikesAnalyticsView(APIView):
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAdminUser]

    queryset = Like.group_by_date().annotate(likes_count=Count('id')).order_by('-agg_date')

    def get(self, request):
        serializer = LikesAnalyticsInputSerializer(data=request.query_params)

        if not serializer.is_valid(False):
            data = []
        else:
            queryset = self.queryset.filter(
                agg_date__gte=serializer.validated_data['date_from'],
                agg_date__lte=serializer.validated_data['date_to']
            )
            data = LikesAnalyticsOutputSerializer(instance=list(queryset), many=True, context=serializer.validated_data).data

        return Response(data)


class UserAnalyticsView(APIView):
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAdminUser]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

        return Response(UserAnalyticsSerializer(instance=user).data)
