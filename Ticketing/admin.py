from django.contrib import admin
from .models import Ticket


admin.site.register(Ticket)

class AuthorAdmin(admin.ModelAdmin):
    list_display = (['title'])
# Register your models here.
