from fastapi import FastAPI
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from models import *

router = APIRouter()

# Pydantic model
class electronic_Device(BaseModel):
    brand: str
    model: str
    year: int
    color: str

celulares: List[electronic_Device] = []
laptops: List[electronic_Device] = []

# Celulares
@router.post("/celulares/")
def create_celular(celular: electronic_Device):
    celulares.append(celular)
    return {"message": "Celular agregado exitosamente"}

@router.get("/celulares/{model}")
def get_celular(model: str):
    for celular in celulares:
        if celular.model == model:
            return celular
    return {"message": "Celular no encontrado"}

@router.delete("/celulares/{model}")
def delete_celular(model: str):
    for celular in celulares:
        if celular.model == model:
            celulares.remove(celular)
            return {"message": "Celular eliminado exitosamente"}
    return {"message": "Celular no encontrado"}

@router.get("/celulares/")
def get_celulares():
    return celulares

# Laptops
@router.post("/laptops/")
def create_laptop(laptop: electronic_Device):
    laptops.append(laptop)
    return {"message": "Laptop agregada exitosamente"}

@router.get("/laptops/{model}")
def get_laptop(model: str):
    for laptop in laptops:
        if laptop.model == model:
            return laptop
    return {"message": "Laptop no encontrado"}

@router.delete("/laptops/{model}")
def delete_laptop(model: str):
    for laptop in laptops:
        if laptop.model == model:
            laptops.remove(laptop)
            return {"message": "Laptop eliminado exitosamente"}
    return {"message": "Laptop no encontrado"}

@router.get("/laptops/")
def get_laptops():
    return laptops
