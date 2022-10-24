from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User



class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username']

class LoginForm(ModelForm):
    class Meta:
        fields = ['username', 'password']