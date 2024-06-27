# FastAPI + SQLModel Boilerplate

Includes:

- CORS middleware
- `alembic` for SQL management/migration
- `Base` class model
- App settings in `config.py`
- `db/get_session()` for routes that need a `Session` dependency

All necessary dependencies are in the `Pipfile`.

## Running the boilerplate

### Shell + Install

1. `pipenv shell`
2. `pipenv install`

### SQL Models

1. Add/configure your models
2. `alembic revision --autogenerate -m "Initial migration"`
3. `alembic upgrade head`

### Running the app

1. `python3 main.py`
2. Go to `http://localhost:8000/docs` for Swagger docs
