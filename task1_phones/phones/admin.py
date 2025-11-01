from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    """
    Настройка административной панели для модели Phone.
    """
    list_display = ['name', 'price', 'release_date', 'lte_exists']
    list_filter = ['lte_exists', 'release_date']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
