import shutil
from pathlib import Path
from typing import List

from fastapi import FastAPI, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from fastApi.database import models
from fastApi.database.connect import engine, get_db
from fastApi.database.models import TrudovayaKnizhka, WorkInfo, AwardInfo
from fastApi.database.schema import TrudovayaKnizhkaOut, TrudovayaKnizhkaCreate

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


@app.post("/trudovaya_knizhka/", response_model=TrudovayaKnizhkaOut)
def create_trudovaya_knizhka(trudovaya_knizhka: TrudovayaKnizhkaCreate, db: Session = Depends(get_db)):
    db_trudovaya_knizhka = TrudovayaKnizhka(**trudovaya_knizhka.dict(exclude={"work_info", "award_info"}))
    db.add(db_trudovaya_knizhka)
    db.commit()
    db.refresh(db_trudovaya_knizhka)

    for work in trudovaya_knizhka.work_info:
        db_work = WorkInfo(**work.dict(), trudovaya_knizhka_id=db_trudovaya_knizhka.id)
        db.add(db_work)

    for award in trudovaya_knizhka.award_info:
        db_award = AwardInfo(**award.dict(), trudovaya_knizhka_id=db_trudovaya_knizhka.id)
        db.add(db_award)

    db.commit()
    db.refresh(db_trudovaya_knizhka)
    return JSONResponse("Success")


@app.get("/trudovaya_knizhka/latest", response_model=List[TrudovayaKnizhkaOut])
def get_latest_trudovaya_knizhka(db: Session = Depends(get_db)):
    return db.query(TrudovayaKnizhka).order_by(TrudovayaKnizhka.id.desc()).limit(5).all()
