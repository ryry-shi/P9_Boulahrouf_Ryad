from django.shortcuts import render, redirect
from Ticketing.forms import FormReview, FormTicketing
from Ticketing.models import Review, Ticket
from django.core.exceptions import PermissionDenied


def create_ticket(request):
    tickets = Ticket.objects.all()
    if request.method == "POST":
        form = FormTicketing(request.POST, request.FILES)
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return render(
            request, "Ticketing/flux.html", {"form": form, "tickets": tickets}
        )
    else:
        form = FormTicketing()
    return render(request, "Ticketing/create_ticket.html", {"form": form})


def ticket_edit(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    # if request.user != ticket.user:
    #     return redirect("ticketing:flux")
    print(ticket.image)
    if request.method == "POST":
        form = FormTicketing(request.POST, request.FILES, instance=ticket)
        ticket = form.save()
        return redirect("ticketing:flux")

    else:
        form = FormTicketing(instance=ticket)
        return render(
            request, "Ticketing/ticket_edit.html", {"form": form, "ticket": ticket}
        )


def remove_ticket(request, ticket_id):
    review = Ticket.objects.get(pk=ticket_id)
    if review.user == request.user:
        review.delete()
        return redirect("ticketing:posts")
    else:
        raise PermissionDenied()


def create_review(request, ticket_id: int):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == "POST":
        form = FormReview(request.POST)
        review = form.save(commit=False)
        review.user = request.user
        review.ticket = ticket
        review.save()
        return redirect("ticketing:flux")
    else:
        form = FormReview()
        return render(
            request,
            "Ticketing/create_review.html",
            {"form": form, "ticket_id": ticket_id, "ticket": ticket},
        )


def create_ticket_with_review(request):
    if request.method == "POST":
        form_1 = FormTicketing(request.POST, request.FILES)
        form_2 = FormReview(request.POST, request.FILES)
        ticket = form_1.save(commit=False)
        review = form_2.save(commit=False)
        ticket.user = request.user
        review.user = request.user
        review.ticket = ticket
        ticket.save()
        review.save()
        return redirect("ticketing:posts")
    else:
        ticket_form = FormTicketing()
        review_form = FormReview()
        return render(
            request,
            "Ticketing/create_ticket_with_review.html",
            {"ticket_form": ticket_form, "review_form": review_form},
        )


def review_edit(request, review_id: int):
    review = Review.objects.get(pk=review_id)
    if request.method == "POST":
        form = FormReview(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("ticketing:posts")
    else:
        form = FormReview(instance=review)
        return render(
            request, "Ticketing/review_edit.html", {"form": form, "review": review}
        )


def flux_view(request):
    tickets = Ticket.objects.all()
    return render(request, "Ticketing/flux.html", {"tickets": tickets})


def posts_view(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    return render(
        request,
        "Ticketing/posts.html",
        {"user": request.user, "tickets": tickets, "reviews": reviews},
    )


def remove_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    if review.user == request.user:
        review.delete()
        return redirect("ticketing:posts")
    else:
        raise PermissionDenied()
