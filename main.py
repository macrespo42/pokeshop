from fastapi import FastAPI
from catalog.routes import catalog_router

app = FastAPI()

app.include_router(catalog_router)