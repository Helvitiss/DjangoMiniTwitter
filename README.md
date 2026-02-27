# Django Mini Twitter

> Первый pet-проект на Django — упрощённый аналог социальной сети. Создан для отработки ключевых концепций фреймворка: ORM, CBV, аутентификация, кастомная модель пользователя, AJAX.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)

---

## О проекте

Учебная социальная сеть с лентой постов, лайками, комментариями и профилями пользователей. Проект охватывает типичный стек Django-разработки: кастомная модель пользователя, class-based views, работа с медиафайлами, AJAX-запросы без перезагрузки страницы.

---

## Функциональность

- Регистрация и авторизация через встроенный Django Auth
- Кастомная модель пользователя (`AbstractUser`) — никнейм, аватар, уникальный email
- Создание постов, лента в обратном хронологическом порядке
- Лайки без перезагрузки страницы (AJAX + jQuery + `JsonResponse`)
- Комментарии к постам
- Профиль пользователя с его постами
- Поиск по пользователям и содержимому постов

---

## Что практиковалось

| Тема | Как применено |
|---|---|
| ORM | `ForeignKey`, `ManyToManyField`, `filter`, `order_by` |
| CBV | `TemplateView`, `DetailView`, `FormView`, `CreateView` |
| Кастомный User | `AbstractUser`, замена через `AUTH_USER_MODEL` |
| AJAX | Лайки через `$.ajax` + `JsonResponse` без перезагрузки |
| Медиафайлы | Загрузка и отдача аватаров через `MEDIA_ROOT` / `MEDIA_URL` |
| Формы | `ModelForm`, `widget_tweaks` для кастомного рендеринга |
| Миграции | Итеративное изменение схемы через `makemigrations` |

---

## Технологический стек

| | |
|---|---|
| **Backend** | Django 5.1 |
| **База данных** | MySQL 8 |
| **Frontend** | HTML, CSS, jQuery (AJAX) |
| **Шаблоны** | Django Templates + widget_tweaks |

---

## Быстрый старт

```bash
git clone https://github.com/Helvitiss/DjangoMiniTwitter.git
cd DjangoMiniTwitter

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Создай `.env` в корне проекта:

```env
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=your_secret_key
```

Применить миграции и запустить:

```bash
python manage.py migrate
python manage.py runserver
```

Приложение доступно по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Структура проекта

```
pet_project/
├── mainapp/        # Посты, лайки, комментарии, поиск
├── users/          # Кастомный пользователь, регистрация, профиль
└── pet_project/    # Настройки, корневые URL
```

---

## Планы по развитию

- Подписки на пользователей и персональная лента
- Пагинация постов
- Уведомления о лайках и комментариях
- Деплой на сервер

---

## Лицензия

[MIT](LICENSE)
