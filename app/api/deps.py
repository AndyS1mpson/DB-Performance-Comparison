from typing import Generator, Optional

from sqlalchemy.orm import Session

from db.session import SessionLocalPG, SessionDockerPG, SessionRemotePG

def get_db_pg() -> Generator:
    db: Optional[Session] = None
    try:
        db = SessionDockerPG()
        yield db
    finally:
        if db is not None:
            db.close()
        

def get_local_pg() -> Generator:
    db: Optional[Session] = None
    try:
        db = SessionLocalPG()
        yield db
    finally:
        if db is not None:
            db.close()


def get_remote_pg() -> Generator:
    db: Optional[Session] = None
    try:
        db = SessionRemotePG()
        yield db
    finally:
        if db is not None:
            db.close()
