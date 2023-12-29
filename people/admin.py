from django.contrib import admin

from .models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_created')
