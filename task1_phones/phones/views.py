from django.shortcuts import render, get_object_or_404
from .models import Phone


def phone_list(request):
    """
    Представление для отображения списка всех телефонов.
    """
    phones = Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, 'phones/phone_list.html', context)


def phone_detail(request, slug):
    """
    Представление для отображения детальной информации о телефоне.
    
    Args:
        slug: уникальный идентификатор телефона
    """
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, 'phones/phone_detail.html', context)
