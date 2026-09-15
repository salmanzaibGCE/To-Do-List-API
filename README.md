# Simple To-Do List API

A minimal REST API for managing tasks. Built with Python + Flask.
Runs in Docker. Designed for CI with GitHub Actions.

## How to Run

### Local

```bash
pip install -r requirements.txt
python app.py
```

API runs on `http://localhost:5000`

### With Docker

```bash
docker build -t todo-api .
docker run -p 5000:5000 todo-api
```

## Endpoints

| Method | Endpoint            | Description          | Example Body            |
|--------|----------------------|-----------------------|--------------------------|
| GET    | `/tasks`             | List all tasks        | -                        |
| POST   | `/tasks`             | Add a new task        | `{"title": "shopping"}`  |
| PUT    | `/tasks/{id}/done`   | Mark a task as done   | -                        |

### Example requests

```bash
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title":"Interview prep"}'
curl http://localhost:5000/tasks
curl -X PUT http://localhost:5000/tasks/1/done
```

## Reflection

