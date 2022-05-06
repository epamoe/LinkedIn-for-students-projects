from django.urls import path
from . import views

urlpatterns = [
    path('register_student', views.register_student, name="register_student"),
    path('register_investor', views.register_investor, name="register_investor"),
    path('login/',views.login_page),
]
