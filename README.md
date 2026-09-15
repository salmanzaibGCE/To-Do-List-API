                                                                                            
# Simple To-Do List API                                                                [![Build Docker Image](https://github.com/salmanzaibGCE/To-Do-List-API/actions/workflows/docker-build.yml/badge.svg)](https://github.com/salmanzaibGCE/To-Do-List-API/actions/workflows/docker-build.yml)

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

## Reflections
Through this task I learned how to build a simple REST API with Python, containerize it,  and wire up a basic CI pipeline with GitHub Actions.  I built the API with Flask because the task itself was fairly small in scope, and Flask  is lightweight with almost no learning curve compared to a heavier framework it let me  focus on getting the endpoints and Docker/CI parts right rather than fighting the framework.  Flask's built-in server (`app.run`) is only meant for development, so I paired it with  Gunicorn, a production-grade WSGI server, so the app could actually be served properly  inside the container rather than through the dev server.  Writing the Dockerfile taught me how to package the app so it can run consistently in any  environment, regardless of what's installed on the host machine. Writing the GitHub Actions  workflow taught me how a CI pipeline is structured jobs, steps, and triggers and how to  set it up so that every push to `main` automatically builds the Docker image and confirms  it still works.  
If I had another day, I would:  
- Add unit tests (pytest) and run them as a CI step before the build 
- Add a security/quality stage GitLeaks for hardcoded secrets, SonarQube/SonarCloud for code quality, and Trivy for image vulnerability scanning
- Push the built image to a registry Docker Hub  instead of just building it locally in CI, and/or upload it as a workflow artifact so it's retrievable from the run itself
- Add a simple front-end/UI so the API is easier to interact with and demo, rather than only through curl


