from fastapi import APIRouter
from api.controllers import events_controller
from api.controllers import predictions_controller

router=APIRouter()
router.include_router(events_controller.router)
router.include_router(predictions_controller.router)
