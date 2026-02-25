# Portfolio API

Backend-проект для портфолио: REST API с авторизацией, CRUD для задач, AI (чат + RAG).  
Docker, CI/CD (GitHub Actions).

## Стек

- **Python 3.11+**
- **FastAPI** — веб-фреймворк
- **SQLAlchemy 2.0** — ORM (async)
- **SQLite** / **PostgreSQL** — БД
- **JWT** — авторизация
- **OpenAI API** — LLM (чат, RAG)
- **Docker** — контейнеризация
- **GitHub Actions** — CI/CD

## Установка

```bash
# Клонировать репозиторий
git clone https://github.com/gvarch1r/portfolio-backend.git
cd portfolio-backend

# Создать виртуальное окружение
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Установить зависимости
pip install -r requirements.txt
```

## Запуск

### Локально (SQLite)

```bash
uvicorn app.main:app --reload
```

### Docker Compose (PostgreSQL)

```bash
docker compose up --build
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

# AI (опционально, для /api/v1/ai/*)
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
```

## API Endpoints

### Auth
- `POST /api/v1/auth/register` — регистрация
- `POST /api/v1/auth/login` — вход (получить JWT)

### AI (требуется авторизация + OPENAI_API_KEY)
- `POST /api/v1/ai/chat` — чат с LLM
- `POST /api/v1/ai/ask` — RAG: вопрос по документации проекта

### Tasks (требуется авторизация)
- `GET /api/v1/tasks` — список задач
- `POST /api/v1/tasks` — создать задачу
- `GET /api/v1/tasks/{id}` — получить задачу
- `PATCH /api/v1/tasks/{id}` — обновить задачу
- `DELETE /api/v1/tasks/{id}` — удалить задачу

### Пример запросов (curl)

```bash
# Регистрация
curl -X POST http://127.0.0.1:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","username":"user","password":"secret123"}'

# Вход
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user&password=secret123"

# Создать задачу (подставить TOKEN из login)
curl -X POST http://127.0.0.1:8000/api/v1/tasks \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Моя задача","description":"Описание"}'
```

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
│   ├── routers/         # API роутеры
│   └── ai/              # LLM, RAG
├── .github/workflows/   # CI/CD
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## CI/CD

При каждом push в `main` GitHub Actions запускает:

- **test** — pytest на Python 3.11 и 3.12
- **lint** — ruff
- **docker** — сборка Docker-образа

## Roadmap

- [x] Этап 1: Backend (REST API, CRUD, JWT)
- [x] Этап 2: DevOps (Docker, CI/CD)
- [x] Этап 3: AI (чат, RAG)

## Лицензия

MIT
