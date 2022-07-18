from django.forms import ModelForm
from .models import User

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username',"last_name",'password']

class LoginForm(ModelForm):
    class Meta:
        fields = ['username', 'password']