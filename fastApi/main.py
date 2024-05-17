import shutil
from pathlib import Path
from typing import List
from loguru import logger
from fastapi import FastAPI, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from fastApi.database import crud, models, schema
from fastApi.database.connect import engine, get_db

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Путь для сохранения загруженных файлов
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/uploadfiles/")
async def upload_files(file: UploadFile):
    logger.info(file.filename)

    logger.info(f"Uploading {file.filename}")
    # Полный путь для сохранения файла
    file_location = UPLOAD_DIR / file.filename

    # Сохранение файла на сервере
    with file_location.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"info": f"{file.filename} files saved successfully"}