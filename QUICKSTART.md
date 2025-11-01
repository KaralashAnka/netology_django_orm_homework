# Быстрый старт

## ⚠️ Для Windows PowerShell

Если вы используете PowerShell, используйте эти команды:

---

## Задание 1: Каталог телефонов

```powershell
cd task1_phones

# Установка зависимостей
pip install -r requirements.txt

# Миграции
python manage.py makemigrations
python manage.py migrate

# Импорт данных (НОВЫЙ СПОСОБ для Windows)
python manage.py import_phones

# Запуск
python manage.py runserver
```

Откройте: http://127.0.0.1:8000/

---

## Задание 2: Онлайн-библиотека

```powershell
cd task2_books

# Установка зависимостей
pip install -r requirements.txt

# Миграции
python manage.py makemigrations
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Добавление книг (НОВЫЙ СПОСОБ для Windows)
python manage.py add_books

# Запуск
python manage.py runserver
```

Откройте:
- http://127.0.0.1:8000/ - библиотека
- http://127.0.0.1:8000/admin/ - админка

---

## 🐧 Для Linux/Mac

Если вы используете Linux или Mac, можете использовать старые команды:

### Задание 1
```bash
cd task1_phones
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py shell < import_phones.py
python manage.py runserver
```

### Задание 2
```bash
cd task2_books
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell < add_sample_books.py
python manage.py runserver
```

---

## 📝 Альтернативные способы импорта данных

### Способ 1: PowerShell с Get-Content
```powershell
# Для задания 1
Get-Content import_phones.py | python manage.py shell

# Для задания 2
Get-Content add_sample_books.py | python manage.py shell
```

### Способ 2: Через Django shell вручную
```powershell
python manage.py shell
```

#### Для задания 1 (телефоны):
```python
import csv
from datetime import datetime
from phones.models import Phone
from django.utils.text import slugify

Phone.objects.all().delete()

with open('phones.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        Phone.objects.create(
            name=row['name'],
            price=float(row['price']),
            image=row['image'],
            release_date=datetime.strptime(row['release_date'], '%Y-%m-%d').date(),
            lte_exists=row['lte_exists'].lower() in ['true', '1', 'yes'],
            slug=slugify(row['name'])
        )

print(f"Импортировано телефонов: {Phone.objects.count()}")
```

#### Для задания 2 (книги):
```python
from books.models import Book
from datetime import date

Book.objects.all().delete()

books = [
    Book(name="Война и мир", author="Лев Толстой", pub_date=date(1869, 1, 1)),
    Book(name="Преступление и наказание", author="Фёдор Достоевский", pub_date=date(1866, 1, 1)),
    Book(name="Мастер и Маргарита", author="Михаил Булгаков", pub_date=date(1967, 1, 1)),
]

Book.objects.bulk_create(books)
print(f"Добавлено книг: {Book.objects.count()}")
```

---

## 🎯 Рекомендуемый способ (самый простой)

**Используйте Django management команды:**

```powershell
# Задание 1
python manage.py import_phones

# Задание 2  
python manage.py add_books
```

Эти команды работают на всех платформах (Windows, Linux, Mac)!

---

## 🔍 Проверка работы команд

Посмотрите доступные команды:
```powershell
python manage.py help
```

Вы должны увидеть:
- `import_phones` - для задания 1
- `add_books` - для задания 2
