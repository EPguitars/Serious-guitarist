from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("gym", views.gym, name="gym"),
    path("logout/", views.logoutUser, name="logout"),
    path("signup/", views.registration, name="registration"),
    path("create_block/", views.BlockCreate.as_view(), name="create_block"),
    path("card/", views.card, name="card"),
]