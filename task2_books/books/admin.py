from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Настройка административной панели для модели Book.
    """
    list_display = ['name', 'author', 'pub_date']
    list_filter = ['pub_date', 'author']
    search_fields = ['name', 'author']
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']
