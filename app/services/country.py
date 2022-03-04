from typing import List

import db.base as models
import schemas
from psycopg2 import errors as pg_errors
from pydantic import parse_obj_as
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def create_country(db: Session, country: schemas.CountryIn) -> schemas.CountryOut:
    """Create new country.

    Args:
        db:
            db session.
        country:
            country to be created.

    Returns:
        CountryOut:
            created country data.
    """
    new_country = models.Country(**country.dict())
    try:
        models.save(db=db, data=new_country)
    except IntegrityError as e:
        if isinstance(e.orig, pg_errors.UniqueViolation):
            raise Exception("Country with such name has already exist.")
        raise
    return schemas.CountryOut(**new_country.__dict__)


def get_all_citites_of_country(db: Session, country_name: str) -> List[schemas.CityOut]:
    """Get all citites of the country.

    Args:
        db:
            db session.
        country_name:
            name of country.

    Returns:
        List[CityOut]:
            cities of the country.
    """
    cities = db.query(models.City) \
        .filter(models.City.country == country_name).all()
    return parse_obj_as(List[schemas.CityOut], cities)
