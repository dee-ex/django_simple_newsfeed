from django.urls import path
from . import controllers

urlpatterns = [
    path('add_post/', controllers.add_post, name='api-add-post'),
    path('add_like/', controllers.add_like, name='api-add-like'),
    path('add_message/', controllers.add_message, name='api-add-message'),
]