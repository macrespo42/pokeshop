from fastapi import APIRouter

catalog_router = APIRouter(prefix="/catalog", tags=["Catalog"])


@catalog_router.get("/available")
def available_cards():
    return {"available": True}
