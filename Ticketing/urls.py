from django.urls import path
from Ticketing.views import create_ticket, show_ticket, create_review

#ticketing:form
app_name = "ticketing"

urlpatterns = [
    path('ticket/create/', create_ticket, name="create_ticket"),
    path('ticket/<int:ticket_id>/', show_ticket, name="show_ticket"),
    path('ticket/<int:ticket_id>/review/', create_review, name="create_review")
    
]


