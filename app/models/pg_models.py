from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """User model."""
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    country_id = Column(Integer, ForeignKey('country.id'))
    county = relationship("Country", back_populates='users')


class Country(Base):
    """Country model."""
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    users = relationship("User", back_populates='country')
