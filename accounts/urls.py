from django.urls import path
from . import views
urlpatterns = [
    
    path("", views.LoginPageView, name="login"),
    path("Register/", views.RegisterPageView, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    
]