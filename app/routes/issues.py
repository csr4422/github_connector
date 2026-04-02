from fastapi import APIRouter
from app.services import github_client
from app.schemas.issue import CreateIssueRequest, CreateIssueResponse

router = APIRouter()


@router.get("/repos/{owner}/{repo}/issues")
def get_issues(owner: str, repo: str):
    issues = github_client.get(f"/repos/{owner}/{repo}/issues")
    return [
        {
            "number": issue["number"],
            "title": issue["title"],
            "state": issue["state"],
            "body": issue["body"],
            "created_at": issue["created_at"],
            "url": issue["html_url"],
        }
        for issue in issues
    ]

@router.post("/repos/{owner}/{repo}/issues", response_model=CreateIssueResponse)
def create_issue(owner: str, repo: str, issue: CreateIssueRequest):
    return github_client.post(
        f"/repos/{owner}/{repo}/issues",
        body=issue.model_dump(exclude_none=True),
    )   