from container import Container
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class PostParticipantsBody(BaseModel):
    first_name: str
    last_name: str
    pseudo: str
    latitude: float
    longitude: float
    google_maps_link: str
    address: str


class PostParticipantsResponse(BaseModel):
    pass


@router.post(
    "/post_participants",
    # response_model=PostParticipantsResponse,
)
def post_participants(
    body: PostParticipantsBody,
):
    if not (body.latitude and body.longitude) and not body.google_maps_link:
        raise HTTPException(
            status_code=400,
            detail="Either latitude and longitude or google maps link must be provided",
        )
    if body.google_maps_link:
        lat_lon = Container.google_maps_links_converter.get_lat_lon_from_link(
            body.google_maps_link
        )
        body.latitude = lat_lon[0]
        body.longitude = lat_lon[1]
    else:
        if not body.latitude or not body.longitude:
            raise HTTPException(
                status_code=400,
                detail="Both latitude and longitude must be provided if not using google maps link",
            )
    Container.mongodb.insert_participant(body.model_dump())
