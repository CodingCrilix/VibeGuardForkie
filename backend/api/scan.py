#endpoint

from fastapi import APIRouter
from models.contracts import ScanTextRequest, ScanResponse

scan_router = APIRouter()

@scan_router.post("/text", response_model=ScanResponse)
def scan_text(request: ScanTextRequest):
    return { "findings": []}
