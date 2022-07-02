from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CRMUserManager(UserManager):

    def create_manager(self, username, email, password, **extra_fields):

        if not password:
            raise ValueError("The password must be have")

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_manager", True)
        return self._create_user(username, email, password, **extra_fields)


class CRMUser(AbstractUser):

    is_manager = models.BooleanField(default=False)
    objects = CRMUserManager()
