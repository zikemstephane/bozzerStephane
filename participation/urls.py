from django.urls import path
from .views import participer,liste_participants

urlpatterns = [
path('participer/<int:id>/', participer, name='participer'),
path('participants/', liste_participants, name='liste_participants'),
]