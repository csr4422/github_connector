from fastapi import APIRouter
from app.services import github_client
from app.schemas.issues import CreateIssueRequest, CreateIssueResponse

router= APIRouter()

@router.get("repos/{owner}/{repo}/issues")
def get_issues(owner:str,repo:str):
    return github_client.get(f"repos/{owner}/{repo}/issues")