from fastapi import FastAPI
from app.routes import repos, issues

app = FastAPI(
    title="Github Connector",
    description="A Simple cloude connect to Github"
    version="1.0.0."
)