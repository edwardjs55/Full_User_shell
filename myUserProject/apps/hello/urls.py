from django.urls import path
from apps.hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<str:name>", views.hello_there, name="hello"),
    path("hello/", views.hello_there, name="helloNo"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
