from fastapi import FastAPI
from routers.routers import router
from database import Base, engine
import models.models

# Crear instancia de FastAPI
app = FastAPI()

# Incluir las rutas del router
app.include_router(router)

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Mensaje de bienvenida
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de práctica"}