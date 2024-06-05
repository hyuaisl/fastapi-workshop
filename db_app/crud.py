from sqlalchemy.orm import Session
from . import models


def get_items(db: Session):
    return db.query(models.ItemDBModel).all()

def create_item(db: Session, title, description):
    db_item = models.ItemDBModel(
        title=title,
        description=description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id, title, description):
    db_item = db.query(models.ItemDBModel).filter(models.ItemDBModel.id == item_id).first()
    db_item.title = title
    db_item.description = description
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id):
    db_item = db.query(models.ItemDBModel).filter(models.ItemDBModel.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
