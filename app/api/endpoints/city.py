from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import schemas, services
from api.deps import get_db_pg

router = APIRouter()

@router.get(
    "/{id}",
    response_model=schemas.CityOut,
    status_code=status.HTTP_200_OK,
    summary="Retrieve city by id."
)
def get_city_by_id(
    id: int,
    db: Session = Depends(get_db_pg)
) -> schemas.CityOut:
    """Retrieve city by id.

    Args:
        id:
            city id.
        db:
            db session.

    Returns:
        CityOut:
            city.
    """
    return services.get_city_by_id(db=db, city_id=id)

@router.post(
    "/",
    response_model=schemas.CityOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create new city."
)
def create_city(
    city: schemas.CityIn,
    db: Session = Depends(get_db_pg)
) -> schemas.CityOut:
    """Create new city.

    Args:
        city:
            city to be created.
        db:
            db sessiob.

    Returns:
        CityOut:
            created city.
    """
    return services.create_city(db=db, city=city)
