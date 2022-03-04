from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True


class CityIn(BaseSchema):
    """Input city scheme."""
    name: str
    description: str
    country: str


class CityOut(BaseSchema):
    """Output city scheme."""
    id: int
    name: str
    description: str
    country: str


class CountryIn(BaseSchema):
    """Input country scheme."""
    name: str


class CountryOut(BaseSchema):
    """Output country scheme."""
    name: str
