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

# Импорт данных (Способ для Windows)
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

# Добавление книг (Способ для Windows)
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

