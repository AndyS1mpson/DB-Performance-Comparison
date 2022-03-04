from db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Country(Base):
    """Country model."""
    __tablename__ = 'country'

    name = Column(
        String,
        unique=True,
        primary_key=True,
        index=True
    )
    cities = relationship("City", back_populates='city_country')


class City(Base):
    """City model."""
    __tablename__ = 'city'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    description = Column(String)
    country = Column(String, ForeignKey('country.name'))
    city_country = relationship("Country", back_populates='cities')
