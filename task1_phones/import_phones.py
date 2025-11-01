"""
Скрипт для импорта данных о телефонах из CSV файла в базу данных.

Использование:
    python manage.py shell < import_phones.py
"""

import csv
from datetime import datetime
from phones.models import Phone
from django.utils.text import slugify


def import_phones_from_csv(csv_file_path='phones.csv'):
    """
    Импортирует телефоны из CSV файла в базу данных.
    
    Args:
        csv_file_path: путь к CSV файлу
    """
    # Очищаем существующие данные
    Phone.objects.all().delete()
    print("Существующие данные удалены.")
    
    # Открываем и читаем CSV файл
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        phones_created = 0
        
        for row in reader:
            try:
                # Парсим дату
                release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()
                
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
                print(f"✓ Импортирован: {phone.name} (slug: {phone.slug})")
                
            except Exception as e:
                print(f"✗ Ошибка при импорте строки {row}: {e}")
                continue
    
    print(f"\n{'='*50}")
    print(f"Импорт завершен! Добавлено телефонов: {phones_created}")
    print(f"{'='*50}\n")


if __name__ == '__main__':
    # Запускаем импорт
    import_phones_from_csv('phones.csv')
