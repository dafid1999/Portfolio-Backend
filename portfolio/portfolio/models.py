from django.db import models

from .enum import PortfolioTStatus


class Portfolio(models.Model):
    portfolioName = models.CharField(
        max_length=255,
        unique=True,
        error_messages={
            "unique": "A portfolio is already created with this name",
        },
    )
    wlasciciel = models.ForeignKey(
        'accounts.Uzytkownik',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="wlasciciel"
    )
    dataZalozenia = models.DateField(auto_now_add=True)
    wyswietlenia = models.IntegerField()
    status = models.PositiveSmallIntegerField(choices=PortfolioTStatus.choices, default=PortfolioTStatus.EDYTOWANY)

    def __str__(self):
        return self.portfolioName


class Tresc(models.Model):
    tresc = models.CharField(max_length=255)
    portfolio = models.ForeignKey(
        'Portfolio', null=True, on_delete=models.SET_NULL, related_name='portfolio_tresc'
    )

    def __str__(self):
        return self.portfolio


class Filmy(models.Model):
    url = models.CharField(max_length=255)
    portfolio = models.ForeignKey(
        'Portfolio', null=True, on_delete=models.SET_NULL, related_name='portfolio_filmy'
    )

    def __str__(self):
        return self.portfolio


class Zdjecia(models.Model):
    url = models.CharField(max_length=255)
    portfolio = models.ForeignKey(
        'Portfolio', null=True, on_delete=models.SET_NULL, related_name='portfolio_zdjecia'
    )

    def __str__(self):
        return self.portfolio
