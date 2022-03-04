from contextlib import contextmanager

from config.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


def create_postgres_engine() -> Engine:
    """Create postgres engine."""
    return create_engine(settings.DOCKER_POSTGRES_URL, pool_pre_ping=True)



postgres_engine = create_postgres_engine()

engines = {
    "postgres": postgres_engine
}


SessionLocalPG = sessionmaker(
    autocommit=False, autoflush=False, bind=engines["postgres"]
)



@contextmanager
def postgress_session():
    """Create postgress session"""
    session = SessionLocalPG()
    try:
        yield session
    finally:
        session.close()
