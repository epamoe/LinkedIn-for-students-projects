from django.urls import path
from .views import *

urlpatterns = [
    path('register_student', register_student, name="register_student"),
    path('register_investor', register_investor, name="register_investor"),
    path('update_profile_student', update_profile_student, name="update_profile_student"),
    path('update_profile_invest', update_profile_invest, name="update_profile_invest"),
    path('profil_student', profil_student, name="profil_student"),
    path('profil_invest', profil_invest, name="profil_invest"),


]
