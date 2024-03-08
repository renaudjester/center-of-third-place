from container import Container
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class GetParticipantsResponse(BaseModel):
    participants: list[dict]


@router.get(
    "/get_participants",
    response_model=GetParticipantsResponse,
)
def get_participants():
    participants = Container.mongodb.query_participants()
    return GetParticipantsResponse(participants=participants)
