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

@router.get("/users/{username}/repos")
def get_user_repos(username: str):
    repos = github_client.get(f"/users/{username}/repos")
    return [
        {
            "name": repo["name"],
            "description": repo["description"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "visibility": repo["visibility"],
        }
        for repo in repos
    ]
