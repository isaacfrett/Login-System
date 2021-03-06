from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name ="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('home/', views.homePage, name="home"),
    path('', views.homePage, name="home")
]