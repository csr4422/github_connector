from fastapi import FastAPI
from app.routes import repos, issues, users

app = FastAPI(
    title="Github Connector",
    description="A Simple cloude connect to Github",
    version="1.0.0"
)

app.include_router(repos.router)
app.include_router(issues.router)
app.include_router(users.router)
@app.get("/health")
def health_check():
    return{"status":"ok", "message":"Github Connector is running"}
