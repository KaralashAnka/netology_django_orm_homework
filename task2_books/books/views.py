from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):
    """
    Представление для отображения списка книг с возможностью сортировки.
    
    Query параметры:
        order: 'name' - сортировка по названию
               'pub_date' - сортировка по дате публикации (по умолчанию)
    """
    # Получаем параметр сортировки из GET запроса
    order_by = request.GET.get('order', 'pub_date')
    
    # Проверяем корректность параметра сортировки
    if order_by not in ['name', 'pub_date']:
        order_by = 'pub_date'
    
    # Получаем отсортированный список книг
    books = Book.objects.all().order_by(order_by)
    
    context = {
        'books': books,
        'current_order': order_by,
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request, pub_date):
    """
    Представление для отображения детальной информации о книге по дате публикации.
    
    Args:
        pub_date: дата публикации в формате YYYY-MM-DD
    """
    # Получаем книгу по дате публикации (первую найденную)
    book = get_object_or_404(Book, pub_date=pub_date)
    
    # Получаем все книги с этой же датой публикации
    books_on_date = Book.objects.filter(pub_date=pub_date)
    
    # Находим предыдущую и следующую книги по дате
    previous_book = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    next_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    
    context = {
        'book': book,
        'books_on_date': books_on_date,
        'previous_date': previous_book.pub_date if previous_book else None,
        'next_date': next_book.pub_date if next_book else None,
    }
    return render(request, 'books/book_detail.html', context)
