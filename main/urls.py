from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('movies/', views.movies, name='movies'),
    path('tv_series/', views.tv_series, name='tv-series'),
    path('bookmarked/', views.bookmarked, name='bookmarked'),
    path('update_bookmarks/', views.update_bookmarks, name='update_bookmarks'),
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
]
