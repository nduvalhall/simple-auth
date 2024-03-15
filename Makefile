install:
	poetry install

test:
	poetry run pytest -s

dev:
	poetry run uvicorn api:app --host=0.0.0.0 --port=8000 --reload

prod:
	poetry run gunicorn -w 4 -k uvicorn.workers.UvicornWorker api:app
