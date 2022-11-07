from fastapi import APIRouter
import core.var_mongo_provider as mongo_provider
from api.models.prediction import prediction

router = APIRouter(
    prefix="/prediction",
    tags=["Prediccion"],
    responses={404: {"description": "Not found"}},
)

@router.post("")
async def prediction_post(contract:prediction):
    return contract

@router.put("/{id_prediction}")
async def prediction_post(id_prediction:str,contract:prediction):
    return contract
