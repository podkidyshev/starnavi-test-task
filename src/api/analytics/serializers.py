import datetime

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer, ListSerializer, ModelSerializer, DateField, IntegerField

from starnavi.user.models import User


class LikesAnalyticsInputSerializer(Serializer):
    date_from = DateField(required=True)
    date_to = DateField(required=True)

    def validate(self, attrs):
        if attrs['date_from'] > attrs['date_to']:
            raise ValidationError('date_from must be <= date_to')
        return attrs


class LikesAnalyticsOutputListSerializer(ListSerializer):
    def to_representation(self, instance):
        """
        Pad missing dates in groups

        Other possible solutions:
            * use database-specific methods to solve it (like generate_series in PostgreSQL or loops),
            * make db queries for each day in range - the worst solution
        """
        data = super().to_representation(instance)
        return_data = []
        date_to = self.context['date_to']
        date_from = self.context['date_from']

        # iterating from date_to down to date_from
        idx = 0
        sliding_date = datetime.date(year=date_to.year, month=date_to.month, day=date_to.day)
        while sliding_date >= date_from:
            if self.instance[idx]['agg_date'] != sliding_date:
                # no likes at that date
                return_data.append(LikesAnalyticsOutputSerializer.get_default_by_date(sliding_date))
            else:
                # there are likes at that date - move sliding window on array
                return_data.append(data[idx])
                idx += 1

            # move sliding date
            sliding_date -= datetime.timedelta(days=1)

        return return_data


class LikesAnalyticsOutputSerializer(Serializer):
    date = DateField(source='agg_date')
    likes_count = IntegerField()

    class Meta:
        list_serializer_class = LikesAnalyticsOutputListSerializer

    @classmethod
    def get_default_by_date(cls, date):
        return {
            'date': date.isoformat(),
            'likes_count': 0
        }


class UserAnalyticsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'date_joined', 'last_login', 'last_request']
