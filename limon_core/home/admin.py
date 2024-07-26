from django.contrib import admin
from home.models import Publications
# Register your models here.

@admin.register(Publications)
class Publications(admin.ModelAdmin):
    list_display = ['title', 'image', 'text']