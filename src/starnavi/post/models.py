from django.db import models
from django.db.models import Count
from django.db.models.functions import TruncDate

from starnavi.user.models import User


class Post(models.Model):
    id = models.BigAutoField('ID', primary_key=True)

    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Author')

    text = models.TextField('Text', max_length=1000)

    date_created = models.DateTimeField('Created date', auto_now_add=True)
    date_modified = models.DateTimeField('Modified date', auto_now=True)

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

        ordering = ['-date_created']

    @classmethod
    def annotate_likes_count(cls, queryset):
        return queryset.annotate(_likes_count=Count('likes'))

    @property
    def likes_count(self):
        return getattr(self, '_likes_count', None)


class Like(models.Model):
    id = models.BigAutoField('ID', primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    date = models.DateTimeField('Date', auto_now_add=True)

    class Meta:
        db_table = 'likes'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

        unique_together = [
            ['user', 'post']
        ]

    @classmethod
    def group_by_date(cls):
        return cls.objects.annotate(agg_date=TruncDate('date')).values('agg_date')
