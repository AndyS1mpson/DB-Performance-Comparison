from fastapi import APIRouter
from api.endpoints import city, country, performance

api_router = APIRouter()

api_router.include_router(city.router, prefix="/city", tags=["City"])
api_router.include_router(country.router, prefix="/country", tags=["Country"])
api_router.include_router(performance.router, prefix="/performance", tags=["Performance"])
