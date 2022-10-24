from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.db import models

# CHANGEMENT DE CLASSE 
class User(AbstractUser):
    pass

    class Meta:
        constraints = [models.UniqueConstraint(fields=['username'], name='unique username')]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username','password']
# Create your models here.
