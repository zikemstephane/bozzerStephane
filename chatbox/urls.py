# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:destinataire_id>/', views.chatbox, name='chatbox'),
    path('chatboxe/', views.chatboxe, name='chatboxe'),
]
