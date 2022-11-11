from django.forms import ModelForm
from .models import Following
from core.models import User

class FormFollowow(ModelForm):
    class Meta:
        model = Following
        fields = ["followed_user"]


    # def clean_followed_user(self):
    #     username = self.cleaned_data["followed_user"]
    #     user = User.objects.get(username=username)
    #     self.cleaned_data["followed_user"] = user.id
    #     return self.cleaned_data

        


