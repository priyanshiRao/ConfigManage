from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/api", tags=["api"])

@router.post("/", response_model=schemas.Configuration)
def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db, config)

@router.get("/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code)
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.post("/update/{country_code}", response_model=schemas.Configuration)
def update_configuration(country_code: str, config: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.update_configuration(db, country_code, config)
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.delete("/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.delete_configuration(db, country_code)
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config
