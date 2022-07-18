
from django.shortcuts import redirect, render
from following.form import FormFollowow


def followed(request):
    if request.method == "POST":
        followed = FormFollowow(request.POST).save(commit=False)
        followed.user = request.user
        return render(request, "following/view_following.html",{"followed": followed})

    else:
        form = FormFollowow()
    return render(request, "following/create_following.html", {'form': form})

def following_view(request):
    return render(request,"following/followed_view.html",{"user":request.user})
