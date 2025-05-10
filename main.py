from fastapi import FastAPI
from routers.routers import router

# Crear instancia de FastAPI
app = FastAPI()

# Incluir las rutas del router
app.include_router(router)

# Mensaje de bienvenida
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de práctica"}