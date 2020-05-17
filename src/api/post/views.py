from django.db import IntegrityError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from starnavi.post.models import Post, Like

from .serializers import PostSerializer


class PostsViewSet(ModelViewSet):
    serializer_class = PostSerializer
    # restrict patch, post and delete
    http_method_names = ['head', 'get', 'post']

    def get_queryset(self):
        queryset = Post.objects.all()
        if self.action in ('list', 'retrieve'):
            queryset = Post.annotate_likes_count(queryset)
        return queryset

    @action(detail=True, methods=['POST'])
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user

        try:
            Like.objects.create(user=user, post=post)
        except IntegrityError as exc:
            if exc.args and exc.args[0].startswith('UNIQUE'):
                pass
            else:
                raise

        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user

        Like.objects.filter(user=user, post=post).delete()

        return Response()
