# Barber — Django & React

A barbershop application with a Django REST backend and a React + TypeScript frontend.

**Stack:** Python · Django · Django REST Framework · PostgreSQL · React · TypeScript · Vite

## Features

- Customer registration and login.
- Barber profiles, service categories and services.
- Appointment records connecting a customer, barber and service.
- Django administration.
- Tests for registration, password hashing, login and the user model.

## Run locally

Use Python 3.12, Node.js 22.12+ and a running PostgreSQL instance.

```bash
git clone https://github.com/NurmuhammaddAliyev/barber_django.git
cd barber_django
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` on Windows PowerShell or `source .venv/bin/activate` on macOS/Linux.

### Backend

```bash
python -m pip install -r config/requirements.txt
```

Copy `config/.env.example` to `config/.env`. Set your own `SECRET_KEY` and a valid `DATABASE_URL` for an existing local PostgreSQL database. Keep `DEBUG=True` only for local development.

```bash
cd config
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend: [http://127.0.0.1:8000](http://127.0.0.1:8000) · Admin: [/admin/](http://127.0.0.1:8000/admin/)

### Frontend

In another terminal, start from the repository root:

```bash
cd fronted/fronted
npm ci
```

Copy `.env.example` to `.env` in this directory and use:

```dotenv
VITE_API_URL=http://127.0.0.1:8000
```

```bash
npm run dev
```

Open the URL printed by Vite, normally [http://localhost:5173](http://localhost:5173).
The application frontend is in `fronted/fronted/`; the similarly named parent directory is not the application root.

## Project structure

| Directory | Responsibility |
| --- | --- |
| `config/store/` | Users, barbers, categories, services and appointments |
| `config/register/` | Registration and login |
| `config/api/` | REST API |
| `config/config/` | Django settings and routing |
| `fronted/fronted/src/` | React interface and API client |

## Verify changes

From the backend directory:

```bash
python manage.py check
python manage.py test register store
```

From `fronted/fronted/`:

```bash
npm run build
npm run lint
```

## Deployment configuration

The backend accepts `DATABASE_URL`, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS`. Set `VITE_API_URL` to the deployed backend before building the frontend. Review authentication, authorization and hosting configuration before using real customer data.

## Author

[Nurmuhammad Aliyev](https://github.com/NurmuhammaddAliyev) · [Telegram](https://t.me/nurmuhammad252505)
