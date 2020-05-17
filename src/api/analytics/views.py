from django.db.models import Count
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from starnavi.post.models import Like

from .serializers import AnalyticsInputSerializer, AnalyticsOutputSerializer


class AnalyticsView(ListAPIView):
    queryset = Like.group_by_date().annotate(likes_count=Count('id')).order_by('-agg_date')

    def list(self, request, *args, **kwargs):
        serializer = AnalyticsInputSerializer(data=request.query_params)

        if not serializer.is_valid(False):
            data = []
        else:
            queryset = self.queryset.filter(
                agg_date__gte=serializer.validated_data['date_from'],
                agg_date__lte=serializer.validated_data['date_to']
            )
            data = AnalyticsOutputSerializer(instance=list(queryset), many=True, context=serializer.validated_data).data

        return Response(data)
