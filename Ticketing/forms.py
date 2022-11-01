
from django.forms import ModelForm
from .models import Review, Ticket


class FormTicketing(ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]

class FormReview(ModelForm):
    class Meta:
        model = Review
        fields = ["body", "headline", "rating"]
        labels = {"body": "contenu"}