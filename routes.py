from fastapi import APIRouter
from controllers import events_controller
from controllers import predictions_controller
from controllers import users_controller
from controllers import utils_controller

router=APIRouter()
router.include_router(events_controller.router)
router.include_router(predictions_controller.router)
router.include_router(users_controller.router)
router.include_router(utils_controller.router)
