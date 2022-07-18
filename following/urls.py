from django.urls import path
from following.views import followed, following_view


app_name = "following"

urlpatterns = [
    path("followed/", followed, name="followed"),
    path("view_followed", following_view, name="following_view")
]


