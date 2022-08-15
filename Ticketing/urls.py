from django.urls import path
from Ticketing.views import create_ticket, review_edit, create_review_with_response, show

#ticketing:form
app_name = "ticketing"

urlpatterns = [
    path('ticket/create/', create_ticket, name="create_ticket"),
    path('ticket/<int:ticket_id>/review_response/', create_review_with_response, name="create_review_with_response"),
    path('ticket/', show, name="show"),
    path('ticket/<int:ticket_id>/review/', review_edit, name="review_edit"),
]


