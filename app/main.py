from fastapi import FastAPI
from api.router import api_router


app = FastAPI(
    title="DB-Perf-Comparison API",
)


app.include_router(api_router)
