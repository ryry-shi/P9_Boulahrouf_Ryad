from django.shortcuts import render, redirect
from Ticketing.forms import FormReview, FormTicketing
from Ticketing.models import Review, Ticket


def create_ticket(request):
    tickets = Ticket.objects.all()
    if request.method == "POST":
        form = FormTicketing(request.POST).save(commit=False)
        form.user = request.user
        form.save()
        return render(request,"Ticketing/view_ticketing.html", {"form": form,"tickets":tickets})
    else:
        form = FormTicketing() 
    return render(request, "Ticketing/create_ticket.html", {'form': form})

def show(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    return render(request,  "Ticketing/view_ticketing.html", {"user": request.user,"reviews":reviews,"tickets":tickets})



def create_review_with_response(request, ticket_id: int):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == "POST":
        review = FormReview(request.POST).save(commit=False)
        review.ticket = Ticket.objects.get(pk=ticket_id)
        review.user = request.user
        review.save()
        return redirect("ticketing:show")
    else:
        form = FormReview() 
        return render(request, "Ticketing/create_review.html", {"form":form,
        "ticket_id":ticket_id, "ticket":ticket})


def review_edit(request, review_id: int):
    review = Review.objects.get(pk=review_id)
    if request.method == "POST":
        review = FormReview(request.POST).save(commit=False)
        if review.is_valid:
            review.save()
            return render(request,"Ticketing/show_review.html", {"review": review, "review_id":review_id})
    else:
        review = FormReview() 
        return render(request, "Ticketing/review_edit.html", {"review":review, "review_id": review_id})
