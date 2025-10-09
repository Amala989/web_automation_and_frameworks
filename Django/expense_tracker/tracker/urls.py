from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add/", views.add_expense, name="add_expense"),
    path("categories/", views.manage_categories, name="manage_categories"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.custom_login, name="login"),
]
