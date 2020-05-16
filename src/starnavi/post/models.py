from django.db import models

from starnavi.user.models import User


class Post(models.Model):
    id = models.BigAutoField('ID', primary_key=True)

    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Author')

    title = models.CharField('Title', max_length=64)
    description = models.TextField('Description', max_length=1000, blank=True, default='')

    date_created = models.DateTimeField('Created date', auto_now_add=True)
    date_modified = models.DateTimeField('Modified date', auto_now=True)

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


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
