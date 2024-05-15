import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    username = models.EmailField(unique=True)
    USERNAME_FIELD = "username"
    is_confirmed = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"
        db_table = "users"


class PasswordResetModel(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=datetime.datetime.now())
    is_valid = models.BooleanField(default=True)
    reset_code = models.CharField(max_length=8)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'reset_codes'
        verbose_name_plural = 'reset_codes'
