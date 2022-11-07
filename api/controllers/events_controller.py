from fastapi import APIRouter
import core.var_mongo_provider as mongo_provider

router = APIRouter(
    prefix="/events",
    tags=["Eventos"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def get_all_events():
    events=list(mongo_provider.db.games_events.find())
    
    return events
