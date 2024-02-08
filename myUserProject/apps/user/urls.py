from django.urls import path
from apps.user import views

urlpatterns = [
    path("", views.home, name="user"),
    #path("hello/<str:name>", views.hello_there, name="hello"),
    #path("hello/", views.hello_there, name="helloNo"),    
]
