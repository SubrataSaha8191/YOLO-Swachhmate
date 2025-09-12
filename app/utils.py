import os
import uuid
from pathlib import Path
from typing import Optional

from fastapi import UploadFile

UPLOAD_DIR = Path(__file__).resolve().parent.parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

async def save_upload(file: UploadFile) -> str:
    ext = Path(file.filename).suffix or ".jpg"
    filename = f"{uuid.uuid4().hex}{ext}"
    dst = UPLOAD_DIR / filename

    with open(dst, "wb") as f:
        while True:
            chunk = await file.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
    await file.close()
    return str(dst)

async def cleanup_file(path: Optional[str]):
    if not path:
        return
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except Exception:
        pass
