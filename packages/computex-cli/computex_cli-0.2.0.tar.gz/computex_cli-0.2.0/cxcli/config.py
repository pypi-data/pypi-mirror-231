import keyring
import os

from typing import Optional
from pydantic import BaseSettings
from dotenv import load_dotenv


def _credentials_path() -> str:
    home_dir = os.path.expanduser("~")
    cx_dir = os.path.join(home_dir, ".cx")
    if not os.path.exists(cx_dir):
        os.makedirs(cx_dir)
    return os.path.join(cx_dir, "credentials")


class Config(BaseSettings):
    username: Optional[str] = None
    password: Optional[str] = None
    core_api_access_token: Optional[str] = None
    core_api_host: str = "api.computex.co"  # "localhost:8000"
    core_api_public_key: Optional[str] = None
    core_api_refresh_token: Optional[str] = None
    core_api_scheme: str = "https"  # "http"
    credentials_path: str = _credentials_path()

    class Config:
        env_prefix = "COMPUTEX_"


def update_config():
    """Use to update config with external env files."""
    config = Config()
    load_dotenv(config.credentials_path)


def set_local_registry_credentials(registry_username, registry_password):
    """
    Store Docker registry credentials securely using keyring.

    Args:
        registry_username (str): Docker registry username.
        registry_password (str): Docker registry password.
    """
    keyring.set_password("docker_registry", "username", registry_username)
    keyring.set_password("docker_registry", "password", registry_password)


def get_local_registry_credentials():
    """
    Retrieve Docker registry credentials from keyring.

    Returns:
        dict: A dictionary containing registry username and password.
    """
    registry_username = keyring.get_password("docker_registry", "username")
    registry_password = keyring.get_password("docker_registry", "password")

    if not registry_username or not registry_password:
        raise Exception("Docker registry credentials not found. Please log in again.")

    return {
        "registry_username": registry_username,
        "registry_password": registry_password,
    }


update_config()
