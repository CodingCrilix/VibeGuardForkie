from fastapi import FastAPI
from api.scan import scan_router

app = FastAPI()

app.include_router(scan_router, prefix="/scan")

@app.get("/ping")
def ping():
    return {"pong": True}
