from django.forms import ModelForm
from .models import Following

class FormFollowow(ModelForm):
    class Meta:
        model = Following
        fields = ["followed_user"]


