from django.urls import path
from apps.registration import views

urlpatterns = [
    path("", views.index, name="registration"),
    #path("home", views.home, name="home"),
    path("index", views.index, name="index"),
    path("register", views.register, name="register"),
    path("registered", views.registered, name="registered"),
    path("gotologin", views.gotologin, name="gotologin"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("loggedin", views.loggedin, name="loggedin"),
    path("loggedout", views.loggedout, name="loggedout"),
    path("update", views.update, name="update"),
    path("user", views.user, name="user"),
]
