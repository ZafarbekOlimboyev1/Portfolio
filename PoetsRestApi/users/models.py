from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'username'
    email = models.EmailField(max_length=254, unique=True)
    is_confirmed = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'users'


