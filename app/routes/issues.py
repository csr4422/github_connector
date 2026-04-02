from fastapi import APIRouter
from app.services import github_client
from app.schemas.issues import CreateIssueRequest, CreateIssueResponse

router= APIRouter()

@router.get("repos/{owner}/{repo}/issues")
def get_issues(owner:str,repo:str):
    return github_client.get(f"repos/{owner}/{repo}/issues")

@router.post("/repo/{owner}/{repo}/issues",response_model=CreateIssueResponse)
def ceate_issue(owner:str,repo:str,issue:CreateIssueRequest):
    return github_client.post(
        f"repos/{owner}/{repo}/issues",
        body=issue.model_dump(exclude_none=True),
    )
