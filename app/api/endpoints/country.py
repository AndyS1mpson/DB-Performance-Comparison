from typing import List

import schemas, services
from api.deps import get_db_pg
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    "/{name}",
    response_model=List[schemas.CityOut],
    status_code=status.HTTP_200_OK,
    summary="Retrieve cities of the country."
)
def get_cities_of_country(
    name: str,
    db: Session = Depends(get_db_pg)
) -> List[schemas.CityOut]:
    """Get cities of the country with such name.

    Args:
        name:
            country name.
        db:
            db session.

    Returns:
        List[CityOut]:
            cities of the country.
    """
    return services.get_all_citites_of_country(db=db, country_name=name)


@router.post(
    "/",
    response_model=schemas.CountryOut,
    status_code=status.HTTP_200_OK,
    summary="Create new country."
)
def create_country(
    country: schemas.CountryIn,
    db: Session = Depends(get_db_pg)
) -> schemas.CountryOut:
    """Create new country.

    Args:
        country:
            country to be created.
        db:
            db session.

    Returns:
        CountryOut:
            created country.
    """
    return services.create_country(db=db, country=country)
