from fastapi import APIRouter
from api.controllers import events_controller

router=APIRouter()
router.include_router(events_controller.router)
