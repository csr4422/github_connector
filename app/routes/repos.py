from fastapi import APIRouter
from app.services import github_client


router =APIRouter()


@router.get("/repos")
def get_repos():
    repos = github_client.get("/user/repos")
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

@router.get("/repos/{owner}/{repo}/commits")
def get_commits(owner: str, repo: str):
    commits= github_client.get(f"/repos/{owner}/{repo}/commits")
    return [
        {
            "sha": commit["sha"],
            "message": commit["commit"]["message"],
            "author": commit["commit"]["author"]["name"],
            "date": commit["commit"]["author"]["date"],
        }
        for commit in commits
    ]