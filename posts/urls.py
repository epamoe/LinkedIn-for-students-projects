from django.urls import path
from .views import *

urlpatterns = [
    path('', accueil, name="accueil"),
    path('index', index, name="index"),
]
