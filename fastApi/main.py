import shutil
from pathlib import Path
from typing import List

from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from sqlalchemy.orm import Session, joinedload
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
async def upload_files(files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    logger.info(files)
    for file in files:
        logger.info(f"Uploading {file.filename}")
        # Полный путь для сохранения файла
        file_location = UPLOAD_DIR / file.filename

        # Сохранение файла на сервере
        with file_location.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    last_knizhka = db.query(TrudovayaKnizhka).order_by(TrudovayaKnizhka.id.desc()).first()
    return {"last_trudovaya_knizhka_id": last_knizhka.id if last_knizhka else None}


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


@app.get("/trudovaya_knizhka/{id}", response_model=TrudovayaKnizhkaOut)
def get_trudovaya_knizhka_by_id(id: int, db: Session = Depends(get_db)):
    trudovaya_knizhka = db.query(TrudovayaKnizhka).options(
        joinedload(TrudovayaKnizhka.work_info),
        joinedload(TrudovayaKnizhka.award_info)
    ).filter(TrudovayaKnizhka.id == id).first()

    if not trudovaya_knizhka:
        raise HTTPException(status_code=404, detail="Trudovaya Knizhka not found")
    return trudovaya_knizhka


@app.put("/trudovaya_knizhka/{id}", response_model=TrudovayaKnizhkaOut)
def update_trudovaya_knizhka(id: int, trudovaya_knizhka: TrudovayaKnizhkaOut, db: Session = Depends(get_db)):
    db_trudovaya_knizhka = db.query(TrudovayaKnizhka).filter(TrudovayaKnizhka.id == id).first()
    if not db_trudovaya_knizhka:
        raise HTTPException(status_code=404, detail="Trudovaya Knizhka not found")

    for key, value in trudovaya_knizhka.dict(exclude_unset=True, exclude={"work_info", "award_info"}).items():
        setattr(db_trudovaya_knizhka, key, value)

    if trudovaya_knizhka.work_info is not None:
        db.query(WorkInfo).filter(WorkInfo.trudovaya_knizhka_id == id).delete()
        for work in trudovaya_knizhka.work_info:
            db_work = WorkInfo(**work.dict(), trudovaya_knizhka_id=id)
            db.add(db_work)

    if trudovaya_knizhka.award_info is not None:
        db.query(AwardInfo).filter(AwardInfo.trudovaya_knizhka_id == id).delete()
        for award in trudovaya_knizhka.award_info:
            db_award = AwardInfo(**award.dict(), trudovaya_knizhka_id=id)
            db.add(db_award)

    db.commit()
    db.refresh(db_trudovaya_knizhka)
    return db_trudovaya_knizhka
