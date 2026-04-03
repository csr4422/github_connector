# GitHub Connector

A simple REST API that connects to GitHub using a Personal Access Token (PAT).

Built with Python and FastAPI.

---

## Setup

1. Clone the repo
git clone https://github.com/csr4422/github-connector.git
cd github-connector

2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create config file
cp config.example.toml config.toml

5. Add your GitHub token to config.toml
[github]
token = "your_github_pat_here"

6. Run the server
uvicorn app.main:app --reload

7. Open docs
http://localhost:8000/docs

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Check if server is running |
| GET | /user | Get authenticated user info |
| GET | /repos | Get authenticated user repos |
| GET | /users/{username}/repos | Get any user's repos |
| GET | /repos/{owner}/{repo}/issues | List issues in a repo |
| POST | /repos/{owner}/{repo}/issues | Create an issue in a repo |
| GET | /repos/{owner}/{repo}/commits | Get recent commits |

---

## Create Issue — Request Body

{
  "title": "Issue title",
  "body": "Issue description"
}

---

## Tech Stack

- Python 3.11
- FastAPI
- httpx
- Pydantic v2