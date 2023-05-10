from django.contrib import admin
from .models import Review, Ticket


admin.site.register(Ticket)
admin.site.register(Review)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["title"]


# Register your models here.
