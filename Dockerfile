FROM python:3.14

WORKDIR /code

COPY --from=ghcr.io/astral-sh/uv:0.10.4 /uv /uvx /bin/

COPY ./pyproject.toml .
COPY ./uv.lock .

RUN uv sync --locked

COPY . /code/

CMD ["uv", "run", "fastapi", "run", "main.py", "--port", "8080"]
