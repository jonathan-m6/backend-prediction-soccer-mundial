from fastapi import APIRouter, status, HTTPException
from models.prediction import prediction
import core.var_mongo_provider as mongo_provider
import shortuuid

router = APIRouter(
  prefix="/prediction",
  tags=["Prediccion"],
  responses={404: {"description": "Not found"}},
)

@router.post("", status_code=status.HTTP_201_CREATED)
async def prediction_post(contract: prediction):
	prediccion ={**contract.dict(), '_id': shortuuid.uuid()}
	mongo_provider.db.predictions.insert_one(prediccion)
	return contract

@router.put("/{id_prediction}")
async def prediction_post(id_prediction:str,contract:prediction):
	mongo_provider.db.predictions.update_one({'_id':id_prediction }, {'$set': contract.dict()})
	return contract
