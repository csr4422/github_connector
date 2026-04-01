import httpx
from fastapi import HTTPException

from app.config import settings

GITHUB_BASE_URL = settings["github"]["base_url"]
GITHUB_API_VERSION = settings["github"]["api_version"]
GITHUB_TOKEN = settings["github"]["token"]