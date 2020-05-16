from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, is_staff=False):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, is_staff=True):
        return self.create_user(username, email, password, is_staff)
