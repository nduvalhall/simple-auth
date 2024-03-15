FROM python:3.12-slim

RUN apt-get update && apt-get install -y make
RUN pip install poetry 
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

COPY . /app

EXPOSE 8000

CMD ["make", "prod"]
