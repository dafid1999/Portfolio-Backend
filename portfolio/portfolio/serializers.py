from rest_framework import serializers

from .models import Portfolio, Tresc, Filmy, Zdjecia


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('__all__')


class TrescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tresc
        fields = ('__all__')


class FilmySerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmy
        fields = ('__all__')


class ZdjeciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zdjecia
        fields = ('__all__')
