from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.ministries.models import Ministries

class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_minister = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    
    school_class = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Класс"
    )
    ministry = models.ForeignKey(
        Ministries,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    