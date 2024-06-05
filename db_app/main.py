from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/")
async def read_items(db: Session = Depends(get_db)):
    items = crud.get_items(db=db)
    return items

@app.post("/items/")
async def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    return crud.create_item(db=db, title=item.title, description=item.description)

@app.patch("/items/{item_id}")
async def update_item(item_id: int, item: schemas.Item, db: Session = Depends(get_db)):
    return crud.update_item(db=db, item_id=item_id, title=item.title, description=item.description)

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db=db, item_id=item_id)
