from fastapi import APIRouter
from app.services import github_client


router =APIROUTER()

@router.get("/repos")
def get_repo():
    return github_client.get("user/repos")