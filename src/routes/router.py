from fastapi import APIRouter
from routes.get_activities import router as get_activities_router
from routes.get_participants import router as get_participants_router
from routes.get_point_in_the_middle import router as get_point_in_the_middle_router
from routes.post_activity import router as post_activity_router
from routes.post_participant import router as post_participant_router

router = APIRouter(responses={404: {"description": "Not found"}})


router = APIRouter()

router.include_router(get_participants_router)
router.include_router(get_activities_router)
router.include_router(post_activity_router)
router.include_router(post_participant_router)
router.include_router(get_point_in_the_middle_router)
