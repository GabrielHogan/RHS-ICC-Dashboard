from django.contrib import admin

from .models import *


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = '__all__'
