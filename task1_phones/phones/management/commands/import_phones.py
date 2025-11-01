"""
Django management команда для импорта телефонов из CSV файла.

Использование:
    python manage.py import_phones
"""

from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Импортирует телефоны из CSV файла в базу данных'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='phones.csv',
            help='Путь к CSV файлу (по умолчанию: phones.csv)'
        )

    def handle(self, *args, **options):
        csv_file = options['file']
        
        self.stdout.write(self.style.WARNING('Начинаю импорт телефонов...'))
        
        # Очищаем существующие данные
        deleted_count = Phone.objects.all().delete()[0]
        self.stdout.write(
            self.style.WARNING(f'Удалено существующих записей: {deleted_count}')
        )
        
        # Открываем и читаем CSV файл
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                phones_created = 0
                
                for row in reader:
                    try:
                        # Парсим дату
                        release_date = datetime.strptime(
                            row['release_date'], 
                            '%Y-%m-%d'
                        ).date()
                        
                        # Создаем объект Phone
                        phone = Phone(
                            name=row['name'],
                            price=float(row['price']),
                            image=row['image'],
                            release_date=release_date,
                            lte_exists=row['lte_exists'].lower() in ['true', '1', 'yes'],
                            slug=slugify(row['name'])
                        )
                        phone.save()
                        phones_created += 1
                        
                        self.stdout.write(
                            self.style.SUCCESS(
                                f'✓ Импортирован: {phone.name} (slug: {phone.slug})'
                            )
                        )
                        
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f'✗ Ошибка при импорте строки {row}: {e}'
                            )
                        )
                        continue
                
                self.stdout.write(self.style.SUCCESS('=' * 50))
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Импорт завершен! Добавлено телефонов: {phones_created}'
                    )
                )
                self.stdout.write(self.style.SUCCESS('=' * 50))
                
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'Файл {csv_file} не найден!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Ошибка: {e}')
            )
