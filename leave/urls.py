from django.urls import path
from leave import views
from .views import *

urlpatterns = [
    path("create_leave", views.create_leave, name="create_leave"),
    path("get_all_leave", views.get_all_leave, name="get_all_leave"),
    path("edit_leave_with_manager/<int:pk>", views.edit_leave_with_manager, name="edit_leave_with_manager"),
]