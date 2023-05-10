from unicodedata import name
from django.urls import path
from Ticketing.views import (
    create_ticket,
    flux_view,
    posts_view,
    remove_review,
    remove_ticket,
    review_edit,
    create_review,
    review_edit,
    create_ticket_with_review,
    ticket_edit,
)

# ticketing:form
app_name = "ticketing"

urlpatterns = [
    path("ticket/create/", create_ticket, name="create_ticket"),
    path("ticket/create_review/<int:ticket_id>/", create_review, name="create_review"),
    path(
        "create_ticket_with_review/",
        create_ticket_with_review,
        name="create_ticket_with_review",
    ),
    path("ticket/<int:ticket_id>/review/", review_edit, name="review_edit"),
    path("flux/", flux_view, name="flux"),
    path("posts/", posts_view, name="posts"),
    path("ticket_edit/<int:ticket_id>/", ticket_edit, name="ticket_edit"),
    path("review_edit/<int:review_id>/", review_edit, name="review_edit"),
    path("remove_review/<int:review_id>/", remove_review, name="remove_review"),
    path("remove_ticket/<int:ticket_id>/", remove_ticket, name="remove_ticket"),
]
