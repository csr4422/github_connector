import tomllib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_config() -> dict:
    config_path = BASE_DIR / "config.toml"

    if not config_path.exists():
        raise FileNotFoundError(
            "config.toml not found. Copy config.example.toml to config.toml and fill in your token."
        )

    with open(config_path, "rb") as f:
        return tomllib.load(f)


settings = load_config()