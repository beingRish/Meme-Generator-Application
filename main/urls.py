from django.urls import path
from . import views



urlpatterns = [
    path("",views.home, name="home"), # / route
    path("register/",views.register, name="register"), # register route
    path("login/", views.login, name="login"), # login path
    path("logout/", views.logout, name="logout"),
    path("memes/", views.getmemes, name="memes") 
    
    
]

