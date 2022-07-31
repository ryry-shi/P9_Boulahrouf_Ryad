
from django.shortcuts import redirect, render
from Ticketing.forms import FormReview, FormTicketing
from Ticketing.models import Ticket


def create_ticket(request):
        # si la requète est de type post on fais un formulaire vide que on sauvegarde et redirige
        if request.method == "POST":
            ticket = FormTicketing(request.POST).save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("ticketing:show_ticket", ticket_id=ticket.id)
        else:
            form = FormTicketing() 
        return render(request, "Ticketing/create_ticket.html", {'form': form})


def show_ticket(request, ticket_id: int):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, "Ticketing/show_ticket.html", {"ticket": ticket})


def create_review(request, ticket_id: int):
    if request.method == "POST":
        review = FormReview(request.POST).save(commit=False)
        review.ticket = Ticket.objects.get(pk=ticket_id)
        review.user = request.user
        review.save()
        return render(request,"Ticketing/show_review.html", {"review":review, "ticket_id":ticket_id})
    else:
        form = FormReview() 
        return render(request, "Ticketing/create_review.html", {"form":form,
        "ticket_id":ticket_id})

def del_ticketing(request, ticket_id: int):
    form = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':    
        form.delete()
        return redirect('home')
    else:
        return render(request, "Ticketing/del_ticket.html", {"form": form, "ticket_id":ticket_id})


