from fastapi import APIRouter
from app.services import github_client

router = APIRouter()

@router.get("/user")
def get_user():
    user = github_client.get("/user")
    return {
        "login": user["login"],
        "name": user["name"],
        "avatar_url": user["avatar_url"],
        "public_repos": user["public_repos"],
        "followers": user["followers"],
        "following": user["following"],
        "url": user["html_url"],
    }