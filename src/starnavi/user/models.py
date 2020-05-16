from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    id = models.BigAutoField('ID', primary_key=True)

    username = models.CharField('Username', unique=True, max_length=64)
    email = models.EmailField('Email', unique=True)

    is_staff = models.BooleanField('Is staff')

    date_joined = models.DateTimeField('Joined date', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        ordering = ['-date_joined']

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
