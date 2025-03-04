from django.urls import path
from app import views

urlpatterns = [
    # rota, view responsável, nome de referência
    path('', views.home, name='home'),
    path('reviews/', views.reviews, name='reviews'),
]