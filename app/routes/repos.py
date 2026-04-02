from fastapi import APIRouter
from app.services import github_client


router =APIRouter()

@router.get("/repos")
def get_repo():
    return github_client.get("user/repos")

@router.get("/repos/{owner}/{repo}/commits")
def get_commits(owner:str,repo:str):
    return github_client.get(f"/repos/{owner}/{repo}/commits")
