install:
	poetry install

test:
	poetry run pytest -s

dev:
	poetry run uvicorn api:app --host=0.0.0.0 --port=8000 --reload

prod:
	poetry run uvicorn api:app --host=0.0.0.0 --port=8000

build:
	sudo docker build . -t simple-auth

run:
	sudo docker run -d -p 8000:8000 --name simple-auth simple-auth

stop:
	sudo docker stop simple-auth
	sudo docker rm simple-auth

logs:
	sudo docker logs simple-auth -f
