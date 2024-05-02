from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('movies/', views.movies, name='movies'),
    path('tv_series/', views.tv_series, name='tv-series'),
    path('bookmarked/', views.bookmarked, name='bookmarked'),
]
