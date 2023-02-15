from django.db import models


class UserType(models.IntegerChoices):
    ADMINISTRATOR = 1, "Administrator"
    UZYTKOWNIK = 2, "Uzytkownik"
    VIP = 3, "Vip"