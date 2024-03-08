from typing import Literal

from container import Container
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class PostActivitiesBody(BaseModel):
    place_name: str
    activity_type: Literal["restaurant", "bar", "museum", "outdoor activity", "other"]
    price_range: Literal["low", "medium", "high"]
    latitude: float
    longitude: float
    google_maps_link: str
    address: str


class PostActivitiesResponse(BaseModel):
    pass


@router.post(
    "/post_activities",
    # response_model=PostActivitiesResponse,
)
def post_activities(
    body: PostActivitiesBody,
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
    Container.mongodb.insert_place(body.model_dump())
