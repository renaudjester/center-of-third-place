from container import Container
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class GetActivitiesBasedOnDistanceFromCenterResponse(BaseModel):
    list_of_activities: list[dict]


@router.get(
    "/get_meeting_point",
    response_model=GetActivitiesBasedOnDistanceFromCenterResponse,
)
def get_meeting_point():
    participants_coordinates = [
        (participant["latitude"], participant["longitude"])
        for participant in Container.mongodb.query_participants()
    ]
    meeting_point = Container.centroid_calculator.calculate_centeroid(
        participants_coordinates
    )
    activities = Container.mongodb.query_places()
    list_of_activities = sorted(
        activities,
        key=lambda activity: Container.centroid_calculator.distance_between_points(
            meeting_point, (activity["latitude"], activity["longitude"])
        ),
    )
    return GetActivitiesBasedOnDistanceFromCenterResponse(
        list_of_activities=list_of_activities
    )
