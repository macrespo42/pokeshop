from fastapi import FastAPI

from interface.api.routes.catalog_routes import router as catalogue_router

app = FastAPI(title="Pokeshop")

app.include_router(catalogue_router)
