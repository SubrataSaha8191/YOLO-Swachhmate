from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="YOLOv8 Garbage Detection API 🚀")
app.include_router(router)

@app.get("/")
def root():
    return {"status": "API running"}
