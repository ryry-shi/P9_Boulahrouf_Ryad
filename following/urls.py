from unicodedata import name
from django.urls import path
from following.views import follow, following_view, followed_table, del_ticketing


app_name = "following"

urlpatterns = [
    path("follow/", follow, name="follow"),
    path("view_followed/", following_view, name="following_view"),
    path('followed_table/', followed_table, name="followed_table"),
    path('followed_table/<int:ticket_id>/del_ticketing', del_ticketing, name="del_ticketing")
]


