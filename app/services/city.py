
from typing import List

import db.base as models
import schemas
from pydantic import parse_obj_as
from sqlalchemy.orm import Session


def create_city(db: Session, city: schemas.CityIn) -> schemas.CityOut:
    """Create new city.

    Args:
        db:
            db session.
        city:
            new city.

    Returns:
        CityOut:
            created city data.
    """
    new_city = models.City(**city.dict())
    models.save(db=db, data=new_city)
    return schemas.CityOut(**new_city.__dict__)


def get_city_by_id(db: Session, city_id: int) -> schemas.CityOut:
    """Get city by id.

    Args:
        db:
            db session.
        city_id:
            city id.

    Returns:
        CityOut:
            city data.
    """
    city = db.query(models.City).get(city_id)
    return schemas.CityOut(**city.__dict__)
