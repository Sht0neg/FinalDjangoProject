
# 💼 FinalDjangoProject

**FinalDjangoProject** — это проект веб-платформы, разработанный на Django, который соединяет работодателей и соискателей. Пользователи могут регистрироваться, размещать вакансии, откликаться на них и просматривать подробную информацию в удобном и интуитивном интерфейсе.

---

## 🚀 Основной функционал

- 🔐 Регистрация и авторизация пользователей
- 👤 Пользовательские роли: работодатель / соискатель
- 💼 Размещение, редактирование и удаление вакансий
- 📄 Просмотр и отклик на вакансии
- 🔍 Фильтрация и поиск по вакансиям
- 🗂️ Каталог и карточки вакансий

---

## 🧱 Архитектура проекта

```
FinalDjangoProject/
│
├── final_project/         # Главные настройки и маршруты
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│
├── user/                  # Модуль пользователей
│   ├── models.py          # Профили (Profile)
│   ├── views.py           # Авторизация, регистрация, профиль
│   ├── forms.py
│   └── urls.py
│
├── vacancy/               # Модуль вакансий
│   ├── models.py          # Вакансии
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/             # HTML-шаблоны
├── static/                # Статика: CSS, JS, изображения
└── manage.py
```

---

## 🛠️ Используемые технологии

- Python 3.x
- Django 5.x
- SQLite (по умолчанию)
- HTML, CSS, JavaScript

---

## 🔗 Основные URL-маршруты

| Маршрут                      | Описание |
|-----------------------------|----------|
| `/`                         | Главная страница |
| `/user/login/`              | Вход в систему |
| `/user/registration/`       | Регистрация |
| `/user/account/<id>/`       | Профиль пользователя |
| `/vacancy/catalog/`         | Каталог вакансий |
| `/vacancy/create-vacancies/`| Создание вакансии |
| `/vacancy/add-vacancy/<id>/`| Отклик на вакансию |
| `/vacancy/update-vacancy/`  | Редактирование вакансии |
| `/vacancy/del-vacancy/`     | Удаление вакансии |

---

## 📌 Возможности расширения

- 🌐 Интернационализация (поддержка i18n через gettext)
- 🔄 REST API с использованием Django REST Framework
- 🔐 JWT-авторизация и клиентская SPA-интеграция
- 📧 Email-уведомления
- 📎 Загрузка резюме, система отзывов

## ⚙️ Установка проекта

```bash
git clone <репозиторий>
cd FinalDjangoProject
python -m venv venv
venv\Scripts\activate  # на Windows
source venv/bin/activate  # на Linux/MacOS
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📃 Лицензия

Проект создан в учебных целях. Авторские права принадлежат разработчикам.

---

С любовью к Django ❤️