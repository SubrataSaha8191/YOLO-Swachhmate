from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from app.models.detector import yolo_detect

router = APIRouter()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    detections = await yolo_detect(file)
    return JSONResponse(content={"detections": detections})
