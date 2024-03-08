from container import Container
from fastapi import APIRouter
from logger import logger
from pydantic import BaseModel

router = APIRouter()


class GetActivitiesResponse(BaseModel):
    activities: list[dict]


@router.get(
    "/get_activities",
    response_model=GetActivitiesResponse,
)
def get_activities():
    activities = Container.mongodb.query_places()
    return GetActivitiesResponse(activities=activities)
