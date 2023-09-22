from pydantic import BaseModel

from .service import CoreApiService


class PredictResponse(BaseModel):
    result: dict


class PredictionResponse(BaseModel):
    status: str
    presigned_url: str


class PredictionServiceV1(CoreApiService):
    base_path: str = "/api/v1/predictions"

    def predict(
        self,
        app_name: str,
        data: dict,
    ):
        r = self._post(f"/{app_name}/predict", json=data, params=data)
        # TODO: Add better status checks and failed login reporting.
        r.raise_for_status()
        return PredictResponse(result=r.json())

    def get_prediction(
        self,
        prediction_id: str,
    ):
        r = self._get(f"/prediction/{prediction_id}")
        r.raise_for_status()
        return PredictionResponse(**r.json())
