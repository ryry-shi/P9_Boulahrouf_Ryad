from django.urls import path
from Ticketing.views import create_ticket, del_ticketing, show_ticket, create_review

#ticketing:form
app_name = "ticketing"

urlpatterns = [
    path('ticket/create/', create_ticket, name="create_ticket"),
    path('ticket/<int:ticket_id>/', show_ticket, name="show_ticket"),
    path('ticket/<int:ticket_id>/review/', create_review, name="create_review"),
    path('ticket/<int:ticket_id>/del/', del_ticketing, name="del_ticketing")

    
]


