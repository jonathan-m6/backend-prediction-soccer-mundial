from fastapi import APIRouter
import core.var_mongo_provider as mongo_provider

router = APIRouter(
    prefix="/events",
    tags=["Eventos"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def get_all_events(user_id:str):
    events=list(mongo_provider.db.events.find())
    predictions=list(mongo_provider.db.predictions.find({'user_id':user_id}))
    
    
    return events
