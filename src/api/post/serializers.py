from rest_framework.serializers import ModelSerializer, SlugRelatedField

from starnavi.post.models import Post


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'date_created', 'likes_count']

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['author'] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        post = super().create(validated_data)
        post._likes_count = 0
        return post
