from django.db import models


class PortfolioTStatus(models.IntegerChoices):
    DOSTEPNY = 1, "Dostepny"
    EDYTOWANY= 2, "Edytowany"
    WYGASLY = 3, "Wygasly"

