import shutil
from pathlib import Path
from typing import List
from loguru import logger
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from fastApi.database import crud, models, schema
from fastApi.database.connect import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Путь для сохранения загруженных файлов
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    logger.info(files)
    for file in files:
        logger.info(f"Uploading {file.filename}")
        # Полный путь для сохранения файла
        file_location = UPLOAD_DIR / file.filename

        # Сохранение файла на сервере
        with file_location.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    return {"info": f"{len(files)} files saved successfully"}
