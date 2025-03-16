from fastapi import FastAPI
from .router import api_router_v1

app = FastAPI()


app.include_router(api_router_v1)


@app.get("/", tags=["Index"])
async def index():
    return {"msg": "Concert Booking backend v1"}
