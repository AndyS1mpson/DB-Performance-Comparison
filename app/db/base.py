from sqlalchemy.orm import Session
from models import *
from db.base_class import Base


def save(db: Session, data: Base) -> None:
    """Save data in db and refresh ORM object data.

    Args:
        db:
            db session.
        data:
            data to be saved.
    """
    db.add(data)
    db.commit()
    db.refresh(data)
