from unicodedata import name
from django.urls import path
from following.views import following, remove_following


app_name = "following"

urlpatterns = [
    path("following/", following, name="following"),
    path(
        "remove_following/<int:followed_user_id>/",
        remove_following,
        name="remove_following",
    ),
]
