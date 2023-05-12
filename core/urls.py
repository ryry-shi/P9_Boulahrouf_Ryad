from django.urls import path
from .views import login_view, logout_view, register_view, index_view


urlpatterns = [
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path("", index_view, name="index"),
]
