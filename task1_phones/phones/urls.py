from django.urls import path
from .views import phone_list, phone_detail

app_name = 'phones'

urlpatterns = [
    path('', phone_list, name='phone_list'),
    path('catalog/<slug:slug>/', phone_detail, name='phone_detail'),
]
