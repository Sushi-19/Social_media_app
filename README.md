# Social Media API

A REST API for a social media application built with FastAPI. The API supports user registration, JWT-based authentication, posts, and post voting.

## Features

- User registration and lookup
- Password hashing with bcrypt
- JWT bearer-token authentication
- Create, read, update, and delete posts
- Search, pagination, and vote counts for posts
- Add and remove votes
- PostgreSQL persistence with SQLAlchemy
- Database migrations with Alembic
- Interactive API documentation through FastAPI

## Tech stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic Settings
- JWT (`python-jose`)
- Uvicorn

## Requirements

- Python 3.10 or newer
- PostgreSQL
- `pip`

## Installation

1. Clone the repository and open the project directory:

   ```bash
   git clone "https://github.com/Sushi-19/Social_media_app"
   cd FastAPI
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root. The application reads these settings through `app/config.py`:

```env
database_hostname=localhost
database_port=5432
database_name=your_database_name
database_username=your_database_user
database_password=your_database_password
secret_key=replace_with_a_long_random_secret
algorithm=HS256
access_token_expire_minutes=30
```

Create the PostgreSQL database named in `database_name` before running the migrations.

## Database migrations

Apply all migrations with:

```bash
alembic upgrade head
```

To create a new migration after changing the SQLAlchemy models:

```bash
alembic revision --autogenerate -m "describe the schema change"
alembic upgrade head
```

## Running the API

Start the development server from the project root:

```bash
uvicorn app.main:app --reload
```

The API is then available at <http://127.0.0.1:8000>.

## API documentation

FastAPI generates interactive documentation automatically:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- OpenAPI schema: <http://127.0.0.1:8000/openapi.json>

## Endpoint overview

| Area | Routes | Authentication |
| --- | --- | --- |
| Health/root | `GET /` | Public |
| Authentication | `POST /login` | Public |
| Users | `POST /users/`, `GET /users/{id}` | Registration is public; lookup is public |
| Posts | `GET /posts/`, `POST /posts/`, `GET /posts/{id}`, `PUT /posts/{id}`, `DELETE /posts/{id}` | Bearer token |
| Votes | `POST /vote/` | Bearer token |

For protected routes, first call `POST /login` using the OAuth2 form fields `username` (the user's email) and `password`. Then send the returned token with:

```text
Authorization: Bearer <access_token>
```

## Project structure

```text
.
├── app/
│   ├── main.py          # FastAPI application and middleware
│   ├── config.py        # Environment-based settings
│   ├── database.py      # PostgreSQL engine and sessions
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── oauth2.py        # JWT creation and authentication
│   └── routers/         # Authentication, users, posts, and votes
├── alembic/             # Database migration environment and versions
├── alembic.ini
├── requirements.txt
└── README.md
```

## Development notes

- Run commands from the repository root so the `app` package and `.env` file are resolved correctly.
- Keep `.env` out of version control; it is already listed in `.gitignore`.
- CORS is currently configured to allow all origins for development. Restrict `allow_origins` before deploying to production.
