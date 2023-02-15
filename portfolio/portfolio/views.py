from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Portfolio, Tresc, Filmy, Zdjecia
from .permissions import AuthenticatedPermissions
from .serializers import PortfolioSerializer, TrescSerializer, FilmySerializer, ZdjeciaSerializer


class PortfolioList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        queryset = Portfolio.objects.all()
        portfolio = self.request.query_params.get('project')
        if portfolio is not None:
            queryset = queryset.filter(portfolioName=portfolio)
        return queryset


class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()


class TrescList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TrescSerializer

    def get_queryset(self):
        queryset = Tresc.objects.all()
        tresc = self.request.query_params.get('pk')
        if tresc is not None:
            queryset = queryset.filter(pk=tresc)
        return queryset


class TrescDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AuthenticatedPermissions,)
    serializer_class = TrescSerializer
    queryset = Tresc.objects.all()


class FilmyList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FilmySerializer

    def get_queryset(self):
        queryset = Filmy.objects.all()
        filmy = self.request.query_params.get('pk')
        if filmy is not None:
            queryset = queryset.filter(pk=filmy)
        return queryset


class FilmyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AuthenticatedPermissions,)
    serializer_class = FilmySerializer
    queryset = Filmy.objects.all()


class ZdjeciaList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ZdjeciaSerializer

    def get_queryset(self):
        queryset = Zdjecia.objects.all()
        zdjecia = self.request.query_params.get('pk')
        if zdjecia is not None:
            queryset = queryset.filter(pk=zdjecia)
        return queryset


class ZdjeciaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AuthenticatedPermissions,)
    serializer_class = ZdjeciaSerializer
    queryset = Zdjecia.objects.all()
