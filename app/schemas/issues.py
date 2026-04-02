from pydantic import BaseModel
from typing import Optional


class CreateIssueRequest(BaseModel):
    title: str
    body: Optional[str] = None
    labels: Optional[list[str]] = []


class CreateIssueResponse(BaseModel):
    number: int
    title: str
    url: str
    state: str