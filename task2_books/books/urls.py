from django.urls import path
from .views import book_list, book_detail

app_name = 'books'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('books/<str:pub_date>/', book_detail, name='book_detail'),
]
