from datetime import datetime
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
	fecha_hoy=datetime.utcnow()
	event=mongo_provider.db.events.find_one({'_id':contract.eventId})
	if fecha_hoy>=event["fechaOrder"]:
		responseError={ "_id":"","eventId":"","golesLocal":0,"golesVisita":0,"userId":"","tiemposExtra":False,"penales":False}
		return responseError
	prediccion ={**contract.dict(), '_id': shortuuid.uuid()}
	mongo_provider.db.predictions.insert_one(prediccion)
	return prediccion

@router.put("/{id_prediction}")
async def prediction_put(id_prediction:str,contract:prediction):
	fecha_hoy=datetime.utcnow()
	event=mongo_provider.db.events.find_one({'_id':contract.eventId})
	if fecha_hoy>=event["fechaOrder"]:
		responseError={ "_id":"","eventId":"","golesLocal":0,"golesVisita":0,"userId":"","tiemposExtra":False,"penales":False}
		return responseError
	mongo_provider.db.predictions.update_one({'_id':id_prediction }, {'$set': contract.dict()})
	return {**contract.dict(), '_id': id_prediction}
