from contextlib import contextmanager

from config.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


def create_docker_pg_session() -> Engine:
    """Create engine for docker db."""
    return create_engine(settings.DOCKER_POSTGRES_URL, pool_pre_ping=True)

def create_local_pg_session() -> Engine:
    """Create engine for local db."""
    return create_engine(settings.LOCAL_POSTGRES_URL, pool_pre_ping=True)

def create_remote_pg_session() -> Engine:
    """Create engine for remote db."""
    return create_engine(settings.REMOTE_POSTGRES_URL, pool_pre_ping=True)


docker_pg_engine = create_docker_pg_session()
local_pg_engine = create_local_pg_session()
remote_pg_engine = create_remote_pg_session()

engines = {
    "docker_pg": docker_pg_engine,
    "local_pg": local_pg_engine,
    "remote_pg": remote_pg_engine
}

SessionLocalPG = sessionmaker(
    autocommit=False, autoflush=False, bind=engines["local_pg"]
)

SessionDockerPG = sessionmaker(
    autocommit=False, autoflush=False, bind=engines["docker_pg"]
)

SessionRemotePG = sessionmaker(
    autocommit=False, autoflush=False, bind=engines["remote_pg"]
)


@contextmanager
def docker_postgress_session():
    """Create docker postgress session"""
    session = SessionDockerPG()
    try:
        yield session
    finally:
        session.close()


@contextmanager
def local_postgress_session():
    """Create local postgress session"""
    session = SessionLocalPG()
    try:
        yield session
    finally:
        session.close()


@contextmanager
def remote_postgress_session():
    """Create remote postgress session"""
    session = SessionRemotePG()
    try:
        yield session
    finally:
        session.close()
