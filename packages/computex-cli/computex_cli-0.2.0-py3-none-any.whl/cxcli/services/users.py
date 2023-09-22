from pydantic import BaseModel

from .service import CoreApiService


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str


class RegistryCredentialsResponse(BaseModel):
    registry_username: str
    registry_host: str
    registry_namespace: str


class ChangePasswordResponseSchema(BaseModel):
    message: str


class UserServiceV1(CoreApiService):
    base_path: str = "/api/v1/users"

    def login(self, username: str, password: str) -> LoginResponse:
        r = self._post(
            "/login", json=LoginRequest(email=username, password=password).dict()
        )
        # TODO: Add better status checks and failed login reporting.
        r.raise_for_status()
        j = r.json()
        return LoginResponse(access_token=j["token"], refresh_token=j["refresh_token"])

    def get_registry_credentials(self):
        r = self._get("/registry_credentials")
        r.raise_for_status()
        j = r.json()
        return RegistryCredentialsResponse(
            registry_username=j["registry_username"],
            registry_host=j["registry_host"],
            registry_namespace=j["registry_namespace"],
        )

    def change_password(
        self, old_password: str, new_password: str, confirm_new_password: str
    ) -> ChangePasswordResponseSchema:
        r = self._post(
            "/change_password",
            json={
                "old_password": old_password,
                "new_password": new_password,
                "confirm_new_password": confirm_new_password,
            },
        )
        r.raise_for_status()
        j = r.json()
        return ChangePasswordResponseSchema(message=j["message"])
