# Portfolio API

Backend-проект для портфолио: REST API с авторизацией, CRUD для задач.  
Планируется расширение: Docker, CI/CD, AI (RAG/LLM).

## Стек

- **Python 3.11+**
- **FastAPI** — веб-фреймворк
- **SQLAlchemy 2.0** — ORM (async)
- **SQLite** — БД (для продакшена можно PostgreSQL)
- **JWT** — авторизация
- **Pydantic** — валидация

## Установка

```bash
# Клонировать репозиторий
git clone https://github.com/YOUR_USERNAME/portfolio-backend.git
cd portfolio-backend

# Создать виртуальное окружение
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Установить зависимости
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn app.main:app --reload
```

API будет доступен по адресу: http://127.0.0.1:8000

- Документация (Swagger): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Переменные окружения

Создайте файл `.env` в корне проекта:

```env
SECRET_KEY=your-secret-key
DEBUG=false
DATABASE_URL=sqlite+aiosqlite:///./portfolio.db
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## API Endpoints

### Auth
- `POST /api/v1/auth/register` — регистрация
- `POST /api/v1/auth/login` — вход (получить JWT)

### Tasks (требуется авторизация)
- `GET /api/v1/tasks` — список задач
- `POST /api/v1/tasks` — создать задачу
- `GET /api/v1/tasks/{id}` — получить задачу
- `PATCH /api/v1/tasks/{id}` — обновить задачу
- `DELETE /api/v1/tasks/{id}` — удалить задачу

## Тесты

```bash
pytest
```

## Структура проекта

```
portfolio-backend/
├── app/
│   ├── main.py          # Точка входа
│   ├── config.py        # Настройки
│   ├── database.py      # Подключение к БД
│   ├── auth.py          # JWT, хеширование
│   ├── models/          # SQLAlchemy модели
│   ├── schemas/         # Pydantic схемы
│   └── routers/         # API роутеры
├── tests/
├── requirements.txt
└── README.md
```

## Roadmap

- [x] Этап 1: Backend (REST API, CRUD, JWT)
- [ ] Этап 2: DevOps (Docker, CI/CD, деплой)
- [ ] Этап 3: AI (ML, RAG, LLM)

## Лицензия

MIT
