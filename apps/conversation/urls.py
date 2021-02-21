from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversations, name='conversations'),
    path('<int:userid>/', views.conversation, name='conversation'),
]