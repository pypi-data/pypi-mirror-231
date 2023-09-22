from typing import List, Optional

from pydantic import BaseModel

from .service import CoreApiService


class DeployRequest(BaseModel):
    app_name: str
    container_image: str
    num_cpu_cores: int
    num_gpu: int
    # TODO: Share SKU enums from main repo.
    gpu: str
    # cpu: str
    memory: int
    replicas: int
    model_image: Optional[str]


class DeployServerlessRequest(BaseModel):
    app_name: str
    container_image: str
    num_cpu_cores: int
    num_gpu: int
    # TODO: Share SKU enums from main repo.
    gpu: str
    # cpu: str
    memory: int
    concurrency: int = 1
    min_scale: int = 0
    max_scale: int = 10
    model_image: Optional[str]


class DeployResponse(BaseModel):
    app_name: str


class DeleteResponse(BaseModel):
    # TODO: Needs better definition once the spec starts to settle.
    status: dict


class ListDeploymentsResponse(BaseModel):
    deployments: List[dict]


class LogsResponse(BaseModel):
    logs: dict


class DeploymentServiceV1(CoreApiService):
    base_path: str = "/api/v1/deployments"

    def deploy(self, deploy_request: DeployRequest) -> DeployResponse:
        r = self._post("/deploy", json=deploy_request.dict())
        # TODO: Add better status checks and failed login reporting.
        r.raise_for_status()
        j = r.json()
        return DeployResponse(app_name=j["app_name"])

    def deploy_serverless(
        self,
        deploy_serverless_request: DeployServerlessRequest,
        is_public: bool = False,
    ):
        path = (
            is_public and "/deploy_serverless_public_endpoint" or "/deploy_serverless"
        )
        r = self._post(path, json=deploy_serverless_request.dict())
        # TODO: Add better status checks and failed login reporting.
        r.raise_for_status()

    def list(self) -> ListDeploymentsResponse:
        r = self._get("/deployments")
        # TODO: Add better status checks and failed login reporting.
        r.raise_for_status()
        j = r.json()
        return ListDeploymentsResponse(deployments=j["deployments"])

    def delete(self, app_name: str):
        r = self._delete(f"/{app_name}")
        # TODO: Add better status checks and failed login reporting.
        r.raise_for_status()
        j = r.json()
        return DeleteResponse(status=j["status"])

    def logs(self, app_name: str):
        r = self._get(f"/{app_name}/logs")
        # TODO: Add better status checks and failed login reporting.
        r.raise_for_status()
        j = r.json()
        return LogsResponse(logs=j["logs"])
