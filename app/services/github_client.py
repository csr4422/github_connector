import httpx
from fastapi import HTTPException

from app.config import settings

GITHUB_BASE_URL = settings["github"]["base_url"]
GITHUB_API_VERSION = settings["github"]["api_version"]
GITHUB_TOKEN = settings["github"]["token"]


def get_headers() -> dict:
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }


def get(endpoint: str, params: dict = None) -> dict | list:
    url = f"{GITHUB_BASE_URL}{endpoint}"
    try:
        with httpx.Client() as client:
            response = client.get(url, headers=get_headers(), params=params)
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to GitHub. Check your internet connection.",
        )
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="GitHub API request timed out. Please try again.",
        )
    return handle_response(response)


def post(endpoint: str, body: dict) -> dict:
    url = f"{GITHUB_BASE_URL}{endpoint}"
    try:
        with httpx.Client() as client:
            response = client.post(url, headers=get_headers(), json=body)
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to GitHub. Check your internet connection.",
        )
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="GitHub API request timed out. Please try again.",
        )
    return handle_response(response)


def handle_response(response: httpx.Response) -> dict | list:
    if response.status_code == 401:
        raise HTTPException(
            status_code=401,
            detail="GitHub authentication failed. Check your token in config.toml.",
        )
    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Resource not found. Check the owner and repo name.",
        )
    if response.status_code == 422:
        raise HTTPException(
            status_code=422,
            detail="Invalid data sent to GitHub. Check your request body.",
        )
    if not response.is_success:
        raise HTTPException(
            status_code=502,
            detail=f"GitHub API error: {response.status_code} — {response.text}",
        )
    return response.json()