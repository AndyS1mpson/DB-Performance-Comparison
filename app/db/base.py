from sqlalchemy.orm import Session
from models import *


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
    db.refresh()
