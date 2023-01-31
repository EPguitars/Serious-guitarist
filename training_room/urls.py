from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("logout/", views.logoutUser, name="logout"),
    path("signup/", views.registration, name="registration"),
    path("create_block/", views.BlockCreate.as_view(), name="create_block"),
    path("card/", views.card, name="card"),
    path("update/<int:pk>/", views.UpdateBlock.as_view(), name="update_block"),
    path("gym", views.ListBlocks.as_view(), name="list_blocks"),
    path("<int:pk>/delete", views.DeleteBlocks.as_view(), name="delete_block"),
]