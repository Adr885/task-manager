# Task Manager API

A simple Task Management REST API built with **FastAPI**, **SQLAlchemy**, **Alembic**, and **PostgreSQL**.
Includes JWT-based authentication so each user only sees their own tasks.

## Tech Stack
- Python 3
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic

## Setup Instructions

### 1. Clone and enter the project
```bash
git clone <your-repo-url>
cd task-manager
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL
Create a database:
```sql
CREATE DATABASE task_manager;
```

### 5. Configure environment variables
```bash
cp .env.example .env
```
Then edit `.env` and set your real `DATABASE_URL` and a strong `SECRET_KEY`.

### 6. Run the database migration
```bash
alembic upgrade head
```

### 7. Start the server
```bash
uvicorn app.main:app --reload
```

### 8. Open the interactive docs
Visit: **http://127.0.0.1:8000/docs**

## API Overview

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Create a new user |
| POST | `/auth/login` | Log in, returns a JWT access token |

### Tasks (require `Authorization: Bearer <token>` header)
| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Get all tasks for the logged-in user |
| GET | `/tasks/{id}` | Get one task by ID |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Database Schema (ERD)

```
users                    tasks
-----                    -----
id (PK)          ┌──────>owner_id (FK -> users.id)
email                     id (PK)
hashed_password           title
                           description
                           status
                           created_at
```

One user **has many** tasks. Each task belongs to exactly one user.
Tasks are only visible to their owner, enforced at the query level in `task_service.py`.

## Generating a new migration after changing models
```bash
alembic revision --autogenerate -m "describe your change"
alembic upgrade head
```
