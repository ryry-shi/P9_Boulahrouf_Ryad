import re
from django.shortcuts import redirect, render
from following.models import Following
from core.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def following(request):
    followings = request.user.followings.all()
    followers = request.user.followers.all()
    if request.method == "POST":
        username = request.POST.get("followed_user")
        if username != request.user.username:
            try:
                followed_user = User.objects.get(username=username)
                following = Following(user=request.user, followed_user=followed_user)
                if Following.objects.filter(user=request.user, followed_user=followed_user).exists():
                    messages.error(request, f"Utilisateur { username } existe")
                following.save()
            except ObjectDoesNotExist:
                messages.error(request, f"Utilisateur { username } n'existe pas .")
    return render(
        request,
        "following/following.html",
        {"followings": followings, "followers": followers},
    )


def remove_following(request, followed_user_id):
    followed_user_id = User.objects.get(pk=followed_user_id)
    following = Following.objects.get(
        user=request.user, followed_user_id=followed_user_id
    )
    following.delete()
    return redirect("following:following")
