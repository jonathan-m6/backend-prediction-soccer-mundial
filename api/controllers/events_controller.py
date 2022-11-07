from fastapi import APIRouter
import core.var_env as variables

router = APIRouter(
    prefix="/events",
    tags=["Eventos"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def get_all_events():
    events=list(variables.db.games_events.find())
    
    return events
