from container import Container
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class GetMeetingPointResponse(BaseModel):
    meeting_point_lattitude: float
    meeting_point_longitude: float


@router.get(
    "/get_meeting_point",
    response_model=GetMeetingPointResponse,
)
def get_meeting_point():
    participants_coordinates = [
        (participant["latitude"], participant["longitude"])
        for participant in Container.mongodb.query_participants()
    ]
    meeting_point = Container.centroid_calculator.calculate_centeroid(
        participants_coordinates
    )
    return GetMeetingPointResponse(
        meeting_point_lattitude=meeting_point[0],
        meeting_point_longitude=meeting_point[1],
    )
