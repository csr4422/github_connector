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

    with httpx.Client() as client:
        response = client.get(url, headers=get_headers(), params=params)

    return handle_response(response)


def post(endpoint: str, body: dict) -> dict:
    url = f"{GITHUB_BASE_URL}{endpoint}"

    with httpx.Client() as client:
        response = client.post(url, headers=get_headers(), json=body)

    return handle_response(response)