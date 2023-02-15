from django.urls import path


from .views import PortfolioList, PortfolioDetail, ZdjeciaDetail, ZdjeciaList, FilmyList, FilmyDetail
from .views import TrescList, TrescDetail

urlpatterns = [
    path('portfolio/', PortfolioList.as_view()),
    path('portfolio/<int:pk>/', PortfolioDetail.as_view()),
    path('tresc', TrescList.as_view()),
    path('tresc/<int:pk>/', TrescDetail.as_view()),
    path('filmy', FilmyList.as_view()),
    path('filmy/<int:pk>/', FilmyDetail.as_view()),
    path('zdjecia', ZdjeciaList.as_view()),
    path('zdjecia/<int:pk>/', ZdjeciaDetail.as_view()),
]