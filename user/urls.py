from django.urls import path
from user import views
from .views import *

urlpatterns = [
    path("create_person", views.create_person, name="create_person"),
    path("get_alluser", views.get_alluser, name="get_alluser"),
    path("login_view", views.login_view, name="login_view"),
]
