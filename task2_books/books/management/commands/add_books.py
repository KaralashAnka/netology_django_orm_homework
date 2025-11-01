"""
Django management команда для добавления тестовых книг в библиотеку.

Использование:
    python manage.py add_books
"""

from django.core.management.base import BaseCommand
from books.models import Book
from datetime import date


class Command(BaseCommand):
    help = 'Добавляет тестовые книги в библиотеку'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Начинаю добавление книг...'))
        
        # Очищаем существующие данные
        deleted_count = Book.objects.all().delete()[0]
        self.stdout.write(
            self.style.WARNING(f'Удалено существующих записей: {deleted_count}\n')
        )
        
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
                'pub_date': date(1869, 1, 1)
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
                'pub_date': date(1836, 1, 1)
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
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Добавлена: {book.name} - {book.author} ({book.pub_date.year})'
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f'✗ Ошибка при добавлении книги {book_data["name"]}: {e}'
                    )
                )
        
        self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
        self.stdout.write(
            self.style.SUCCESS(f'Добавление завершено! Всего книг: {books_created}')
        )
        self.stdout.write(self.style.SUCCESS('=' * 60 + '\n'))
        
        # Дополнительная информация
        self.stdout.write(self.style.WARNING('Примечания:'))
        self.stdout.write('- Несколько книг имеют одинаковые даты публикации')
        self.stdout.write('- Книги доступны по адресу: http://127.0.0.1:8000/')
        self.stdout.write('- Сортировка: ?order=name или ?order=pub_date')
