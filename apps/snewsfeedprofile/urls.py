from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('follow/', views.follow, name='follow'),
    path('unfollow/', views.unfollow, name='unfollow'),
    path('followers/', views.followers, name='followers'),
    path('follows/', views.follows, name='follows'),
]