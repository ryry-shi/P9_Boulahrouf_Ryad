from django.shortcuts import redirect, render
from following.form import FormFollowow
from following.models import Following



def follow(request):
    if request.method == "POST":
        form = FormFollowow(request.POST).save(commit=False)
        form.user = request.user
        form.save()
        return render(request, "following/view_following.html", {"form":form})
    else:
        form = FormFollowow() 
    return render(request, "following/create_following.html", {'form': form})

def following_view(request):
    return render(request,"following/followed_view.html",{"user":request.user})

def followed_delete(request):
    form = request.user
    if request.method == 'POST':    
        form.delete()
        return redirect('home')
    else:
        return render(request, "following/followed_delete.html", {"form": form})

# créer une vue avec les utilisateur suivis et les mettre dans un tableau pour pouvoir les mettre sur une page

def followed_table(request):
    # followings = Following.objects.filter(user=request.user)
    followings = request.user.followings.all()
    followers = request.user.followers.all()
    if request.method == "POST":
        form = FormFollowow(request.POST).save(commit=False)
        form.user = request.user
        form.save()
        return render(request, "following/followed_table.html", {'followings': followings, 'followers':followers, "form":form})
    else:
        form = FormFollowow()
    return render(request, "following/followed_table.html", {'form':form,'followings': followings, 'followers':followers})


def del_ticketing(request, ticket_id: int):
    form = Following.objects.get(pk=ticket_id)
    if request.method == 'POST':    
        form.delete()
        return redirect('home')
    else:
        return render(request, "following/del_following.html", {"form": form, "ticket_id":ticket_id})
