from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import toml
import uvicorn

from . import routes


config = toml.load("config.toml")["api"]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)


def dev():
    uvicorn.run(
        app,
        host=config["host"],
        port=config["port"],
        reload=True,
    )


def prod():
    uvicorn.run(
        app,
        host=config["host"],
        port=config["port"],
        workers=config["workers"],
    )
