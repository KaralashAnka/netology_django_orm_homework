"""
Скрипт для добавления тестовых книг в библиотеку.

Использование:
    python manage.py shell < add_sample_books.py
"""

from books.models import Book
from datetime import date


def add_sample_books():
    """
    Добавляет тестовые книги в базу данных.
    """
    # Очищаем существующие данные
    Book.objects.all().delete()
    print("Существующие книги удалены.\n")
    
    # Список книг для добавления
    books_data = [
        {
            'name': 'Война и мир',
            'author': 'Лев Толстой',
            'pub_date': date(1869, 1, 1)
        },
        {
            'name': 'Анна Каренина',
            'author': 'Лев Толстой',
            'pub_date': date(1877, 1, 1)
        },
        {
            'name': 'Преступление и наказание',
            'author': 'Фёдор Достоевский',
            'pub_date': date(1866, 1, 1)
        },
        {
            'name': 'Братья Карамазовы',
            'author': 'Фёдор Достоевский',
            'pub_date': date(1880, 1, 1)
        },
        {
            'name': 'Идиот',
            'author': 'Фёдор Достоевский',
            'pub_date': date(1869, 1, 1)  # Та же дата что и "Война и мир"
        },
        {
            'name': 'Мастер и Маргарита',
            'author': 'Михаил Булгаков',
            'pub_date': date(1967, 1, 1)
        },
        {
            'name': 'Собачье сердце',
            'author': 'Михаил Булгаков',
            'pub_date': date(1925, 1, 1)
        },
        {
            'name': 'Евгений Онегин',
            'author': 'Александр Пушкин',
            'pub_date': date(1833, 1, 1)
        },
        {
            'name': 'Капитанская дочка',
            'author': 'Александр Пушкин',
            'pub_date': date(1836, 1, 1)
        },
        {
            'name': 'Мёртвые души',
            'author': 'Николай Гоголь',
            'pub_date': date(1842, 1, 1)
        },
        {
            'name': 'Ревизор',
            'author': 'Николай Гоголь',
            'pub_date': date(1836, 1, 1)  # Та же дата что и "Капитанская дочка"
        },
        {
            'name': 'Отцы и дети',
            'author': 'Иван Тургенев',
            'pub_date': date(1862, 1, 1)
        },
        {
            'name': 'Вишнёвый сад',
            'author': 'Антон Чехов',
            'pub_date': date(1904, 1, 1)
        },
        {
            'name': 'Тихий Дон',
            'author': 'Михаил Шолохов',
            'pub_date': date(1940, 1, 1)
        },
        {
            'name': 'Доктор Живаго',
            'author': 'Борис Пастернак',
            'pub_date': date(1957, 1, 1)
        },
    ]
    
    books_created = 0
    
    # Создаём книги
    for book_data in books_data:
        try:
            book = Book.objects.create(**book_data)
            books_created += 1
            print(f"✓ Добавлена: {book.name} - {book.author} ({book.pub_date.year})")
        except Exception as e:
            print(f"✗ Ошибка при добавлении книги {book_data['name']}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Добавление завершено! Всего книг: {books_created}")
    print(f"{'='*60}\n")
    
    # Дополнительная информация
    print("Примечания:")
    print("- Несколько книг имеют одинаковые даты публикации для демонстрации функционала")
    print("- Книги можно просмотреть по адресу: http://127.0.0.1:8000/")
    print("- Сортировка доступна через параметры: ?order=name или ?order=pub_date")
    print()


if __name__ == '__main__':
    add_sample_books()
