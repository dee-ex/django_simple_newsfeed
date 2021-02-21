from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('search/', views.search, name='search')
]