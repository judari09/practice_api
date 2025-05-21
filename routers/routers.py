from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from models.models import Device

router = APIRouter()

class ElectronicDevice(BaseModel):
    brand: str
    model: str
    year: int
    color: str

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Celulares
@router.post("/celulares/")
def create_celular(celular: ElectronicDevice, db: Session = Depends(get_db)):
    db_device = Device(**celular.dict(), type="celular")
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return {"message": "Celular agregado exitosamente"}

@router.get("/celulares/{model}", response_model=ElectronicDevice)
def get_celular(model: str, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.model == model, Device.type == "celular").first()
    if device:
        return device
    raise HTTPException(status_code=404, detail="Celular no encontrado")

@router.delete("/celulares/{model}")
def delete_celular(model: str, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.model == model, Device.type == "celular").first()
    if device:
        db.delete(device)
        db.commit()
        return {"message": "Celular eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Celular no encontrado")

@router.get("/celulares/", response_model=List[ElectronicDevice])
def get_celulares(db: Session = Depends(get_db)):
    return db.query(Device).filter(Device.type == "celular").all()

# Laptops
@router.post("/laptops/")
def create_laptop(laptop: ElectronicDevice, db: Session = Depends(get_db)):
    db_device = Device(**laptop.dict(), type="laptop")
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return {"message": "Laptop agregada exitosamente"}

@router.get("/laptops/{model}", response_model=ElectronicDevice)
def get_laptop(model: str, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.model == model, Device.type == "laptop").first()
    if device:
        return device
    raise HTTPException(status_code=404, detail="Laptop no encontrada")

@router.delete("/laptops/{model}")
def delete_laptop(model: str, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.model == model, Device.type == "laptop").first()
    if device:
        db.delete(device)
        db.commit()
        return {"message": "Laptop eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Laptop no encontrada")

@router.get("/laptops/", response_model=List[ElectronicDevice])
def get_laptops(db: Session = Depends(get_db)):
    return db.query(Device).filter(Device.type == "laptop").all()
