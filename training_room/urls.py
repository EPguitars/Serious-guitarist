from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("gym", views.gym, name="gym"),
]