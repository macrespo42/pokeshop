FROM python:3.14

WORKDIR /code

COPY --from=ghcr.io/astral-sh/uv:0.10.4 /uv /uvx /bin/

RUN uv sync --locked

COPY . /code/

CMD ["fastapi", "run", "main.py", "--port", "80"]