from django.urls import path
from . import views

urlpatterns = [
    path('register_student/', views.register_student, name="register_student"),
    path('register_investor/', views.register_investor, name="register_investor"),
    path('connexion/', views.connexion, name="connexion"),
    path('profil_student/<str:id_e>', views.profil_student, name="profil_student"),
    path('profil_investor/<str:id_i>', views.profile_investor, name="profile_investor"),
    path('update_profile_investor/',views.update_profile_investor, name="update_profile_investor"),
    path('update_profile_student/',views.update_profile_student, name="update_profile_student"),
    path('user_logout/', views.user_logout, name="user_logout"),
]
