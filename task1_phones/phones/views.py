from django.shortcuts import render, get_object_or_404
from .models import Phone


def phone_list(request):
    """
    Представление для отображения списка всех телефонов с возможностью сортировки.
    
    Query параметры:
        sort: 'name' - сортировка по названию
              'price' - сортировка по цене
              'min_price' - сортировка по цене (по возрастанию)
              'max_price' - сортировка по цене (по убыванию)
    """
    # Получаем параметр сортировки из GET запроса
    sort_by = request.GET.get('sort', 'name')
    
    # Определяем порядок сортировки
    if sort_by == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_by == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        # По умолчанию сортировка по названию
        phones = Phone.objects.all().order_by('name')
    
    context = {
        'phones': phones,
        'current_sort': sort_by,
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
