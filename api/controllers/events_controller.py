from fastapi import APIRouter
from api.serializers.events_serializer import eventEntity, eventListEntity
import core.var_env as variables

router = APIRouter(
    prefix="/events",
    tags=["Eventos"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def get_all_events():
    # events = variables.db.games_events.find()
    events = eventListEntity(variables.db.games_events.find())
    return {'data': events}
