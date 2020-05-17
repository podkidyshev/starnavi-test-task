from rest_framework.serializers import ModelSerializer

from starnavi.post.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'description', 'date_created', 'likes_count']
        read_only_fields = ['author', 'likes_count']

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['author'] = self.context['request'].user
        return attrs
