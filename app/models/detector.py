from ultralytics import YOLO 
import os, uuid, shutil

# Load model once at startup
model = YOLO("weights/best.pt")
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def yolo_detect(file):
    file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = model(file_path, imgsz=640)
    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                "class": model.names[int(box.cls)],
                "confidence": round(float(box.conf), 3),
                "bbox": [round(x, 2) for x in box.xyxy[0].tolist()]
            })

    os.remove(file_path)  # cleanup
    return detections
