from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {"username":"mdp"}


# class LoginForm(ModelForm):
#     class Meta:
#         fields = ['username', 'password']