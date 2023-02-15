from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UzytkownikManager
from .enum import UserType


class Uzytkownik(AbstractUser):
    """Custom user model with e-mail as unique identifiers."""

    username = None
    email = models.EmailField(
        verbose_name="email address",
        unique=True,
        error_messages={
            "unique": "A user is already registered with this email address",
        },
    )
    user_type = models.PositiveSmallIntegerField(choices=UserType.choices, default=UserType.UZYTKOWNIK)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = UzytkownikManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
