# Fugue App

This is a basic file serving app for Fugue.

# Requirements

- [Docker](https://www.docker.com/) (Docker for Mac or Docker-CE/EE)
- [dgoss](https://github.com/aelsabbahy/goss/tree/master/extras/dgoss) - for container tests

# Getting Started

1. Run application acceptance tests.

  ```
  docker run -v ${PWD}:/app -e PYTHONPATH=/app python:2.7  bash -c "pip install -r /app/requirements.txt -r /app/tests/requirements.txt && pytest -v /app/tests"
  ```

2. Next, build a container image.

  ```
  docker build -t fugue_app:latest .
  ```

3. Then, test the container image using dgoss:

  ```
  dgoss run fugue_app:latest
  ```

4. Start the application:

  ```
  docker run --rm -d -p 8080:80 --name my_app fugue_app:latest
  ```

5. Point your web browser to <http://127.0.0.1:8080/>. The index page should be returned.

6. To stop the container:

  ```
  docker kill my_app
  ```

# Endpoints

## `/health`

- Method: GET

  Return Content: JSON blob containing at least `{'status': 'Ok'}` if the service is healthy.

  Success Status Code: 200

## `/`

- Method: GET

  Return Content: Contents of `index.html`

  Success Status Code: 200

## `/<path_to_file>`

- Method: GET

  Return Content: Contents of that file.

  Success Status Code: 200
