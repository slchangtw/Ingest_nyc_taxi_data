FROM prefecthq/prefect:2-python3.10

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /

COPY poetry.lock pyproject.toml ./

RUN pip install -U pip && \
    pip install poetry==1.6.0 && \
    poetry install --no-interaction --no-cache --only main

ENV DOCKER_ENV=True

COPY src/ src/

CMD ["python", "-m", "src.flow"]
