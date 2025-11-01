# Структура проекта - Домашнее задание Django ORM

## 📁 Общая структура

```
netology_django_orm_homework/
│
├── 📄 README.md                    # Главная документация
├── 📄 QUICKSTART.md                # Быстрый старт
├── 📄 EXPLANATION.md               # Подробные пояснения
├── 📄 .gitignore                   # Игнорируемые файлы
│
├── 📁 task1_phones/                # ✅ ЗАДАНИЕ 1 (Обязательное)
│   │
│   ├── 📄 manage.py                # Django management команды
│   ├── 📄 import_phones.py         # 🔧 Скрипт импорта из CSV
│   ├── 📄 phones.csv               # 📊 Данные телефонов
│   ├── 📄 requirements.txt         # Зависимости
│   ├── 📄 README.md                # Документация задания
│   │
│   ├── 📁 phones_project/          # Конфигурация проекта
│   │   ├── __init__.py
│   │   ├── settings.py             # ⚙️ Настройки Django
│   │   ├── urls.py                 # 🔗 Главные URL
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   └── 📁 phones/                  # Django приложение
│       ├── __init__.py
│       ├── models.py               # 📦 Модель Phone
│       ├── views.py                # 👁️ Представления
│       ├── urls.py                 # 🔗 URL маршруты
│       ├── admin.py                # 👔 Админ-панель
│       ├── apps.py
│       │
│       ├── 📁 migrations/          # Миграции БД
│       │   └── __init__.py
│       │
│       └── 📁 templates/phones/    # 🎨 HTML шаблоны
│           ├── base.html
│           ├── phone_list.html
│           └── phone_detail.html
│
└── 📁 task2_books/                 # ✅ ЗАДАНИЕ 2 (Дополнительное)
    │
    ├── 📄 manage.py                # Django management команды
    ├── 📄 add_sample_books.py      # 🔧 Скрипт добавления книг
    ├── 📄 requirements.txt         # Зависимости
    ├── 📄 README.md                # Документация задания
    │
    ├── 📁 books_project/           # Конфигурация проекта
    │   ├── __init__.py
    │   ├── settings.py             # ⚙️ Настройки Django
    │   ├── urls.py                 # 🔗 Главные URL
    │   ├── wsgi.py
    │   └── asgi.py
    │
    └── 📁 books/                   # Django приложение
        ├── __init__.py
        ├── models.py               # 📦 Модель Book
        ├── views.py                # 👁️ Представления
        ├── urls.py                 # 🔗 URL маршруты
        ├── admin.py                # 👔 Админ-панель
        ├── apps.py
        │
        ├── 📁 migrations/          # Миграции БД
        │   └── __init__.py
        │
        └── 📁 templates/books/     # 🎨 HTML шаблоны
            ├── base.html
            ├── book_list.html
            └── book_detail.html
```

---

## 🎯 Задание 1: Каталог телефонов

### Ключевые файлы:

#### 📦 models.py
```python
class Phone(models.Model):
    name           # Название телефона
    price          # Цена (DecimalField)
    image          # URL изображения
    release_date   # Дата выпуска
    lte_exists     # Поддержка LTE
    slug           # Уникальный идентификатор (автогенерация)
```

#### 👁️ views.py
- `phone_list()` - список всех телефонов
- `phone_detail(slug)` - детали по slug

#### 🔗 URLs
```
/                          → phone_list
/catalog/<slug>/          → phone_detail
```

#### 🔧 import_phones.py
- Читает CSV файл (delimiter=';')
- Парсит данные
- Создает объекты Phone
- Генерирует slug автоматически

#### 📊 phones.csv
```csv
name;price;image;release_date;lte_exists
iPhone X;73999;https://...;2017-11-03;true
```

---

## 🎯 Задание 2: Онлайн-библиотека

### Ключевые файлы:

#### 📦 models.py
```python
class Book(models.Model):
    name        # Название книги
    author      # Автор
    pub_date    # Дата публикации
```

#### 👁️ views.py
- `book_list()` - список с сортировкой
  - ?order=name - по названию
  - ?order=pub_date - по дате
- `book_detail(pub_date)` - детали + навигация

#### 🔗 URLs
```
/                          → book_list
/?order=name              → book_list (сортировка)
/?order=pub_date          → book_list (сортировка)
/books/<pub_date>/        → book_detail
```

#### 🔧 add_sample_books.py
- Добавляет 15 тестовых книг
- Русская классика
- Разные даты публикации
- Некоторые книги с одной датой

---

## 📊 Статистика проекта

### Задание 1 (Телефоны)
- ✅ 14 Python файлов
- ✅ 3 HTML шаблона
- ✅ 1 CSV файл с данными
- ✅ Полная документация
- ✅ Административная панель
- ✅ Автоматический импорт

### Задание 2 (Библиотека)
- ✅ 14 Python файлов
- ✅ 3 HTML шаблона
- ✅ Скрипт добавления данных
- ✅ Полная документация
- ✅ Административная панель
- ✅ Сортировка и навигация

---

## 🚀 Быстрый запуск

### Задание 1
```bash
cd task1_phones
pip install -r requirements.txt
python manage.py migrate
python manage.py shell < import_phones.py
python manage.py runserver
```

### Задание 2
```bash
cd task2_books
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py shell < add_sample_books.py
python manage.py runserver
```

---

## 📝 Документация

Каждое задание включает:
1. **README.md** - полная инструкция
2. **Комментарии в коде** - объяснение логики
3. **Docstrings** - документация функций
4. **Примеры использования** - как работать с кодом

---

## 🎨 Особенности UI/UX

### Задание 1 (Телефоны)
- 📱 Адаптивная сетка карточек
- 🖼️ Изображения телефонов
- 💰 Цены в рублях
- 📅 Даты выпуска
- 📡 Значок LTE
- ✨ Анимация при наведении

### Задание 2 (Библиотека)
- 📚 Список книг
- 🔄 Кнопки сортировки
- 🎨 Градиентный дизайн
- 📖 Детальные страницы
- ⬅️➡️ Навигация по датам
- 📅 Группировка по датам

---

## ✅ Соответствие требованиям

### PEP 8
- ✅ Правильные отступы (4 пробела)
- ✅ Длина строк < 120 символов
- ✅ Именование переменных (snake_case)
- ✅ Именование классов (PascalCase)

### Django Best Practices
- ✅ Правильная структура приложений
- ✅ Использование app_name
- ✅ get_object_or_404
- ✅ verbose_name в моделях
- ✅ Meta классы
- ✅ __str__ методы

### Стандарты Нетологии
- ✅ Документация на русском
- ✅ Понятные имена переменных
- ✅ Комментарии где нужно
- ✅ Примеры использования

---

## 🔧 Технологии

- **Python** 3.8+
- **Django** 3.2+
- **SQLite** (БД по умолчанию)
- **HTML/CSS** (шаблоны)
- **CSV** (импорт данных)

---

## 📦 Итого в проекте:

- **28** Python файлов
- **6** HTML шаблонов
- **2** скрипта импорта/добавления данных
- **5** документационных файлов
- **2** requirements.txt
- **1** .gitignore
- **2** полностью рабочих Django приложения

---

## 🎓 Готово к сдаче!

Все задания выполнены в соответствии с требованиями курса "Django: создание функциональных веб-приложений" от Нетологии.
