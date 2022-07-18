from django.contrib.auth.models import AbstractUser
from django.contrib import admin


class User(AbstractUser):
    pass

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username','password']
# Create your models here.
